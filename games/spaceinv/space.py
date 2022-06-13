from tkinter import *

def move_invs(Dir,invs, counter):
  global canvas  
  lost = 0  
  if counter % 20 == 0:    
    Dir *= -1
    for inv in invs:    
      canvas.move(inv,0,25)
      _,cy1 = canvas.coords(inv)
      if cy1 >= 600:
        lost = 1
  else:
    for inv in invs:
      canvas.move(inv,Dir*10,0)
  return Dir, counter, lost


def move_bullets(bullets):
  global canvas
  size = len(bullets)
  i = 0
  while i < size:
    b = bullets[i]
    canvas.move(b,0,-10)
    _,_,_,y2 = canvas.coords(b)
    if y2 <= 0:
      bullets.pop(i)
      canvas.delete(b)
      size -= 1
      i -= 1
    i += 1

def check_col(inv,bullet):
  global canvas
  icx,icy = canvas.coords(inv)
  ix1,ix2 = icx - 15,icx + 15
  iy1,iy2 = icy - 11,icy + 11
  bx1,by1,bx2,by2 = canvas.coords(bullet)
  col = (bx1 <= ix2 and bx2 >= ix1 and  by1 <= iy2 and by2 >= iy1) 
  return col

def check_cols(bullets,invs):
  global canvas
  sizeB = len(bullets)
  tot_cols = 0
  i = 0
  while i < sizeB:
    bullet = bullets[i]

    sizeI = len(invs)
    j = 0
    col  = 0
    while j < sizeI and not col:
      inv = invs[j]

      col = check_col(inv,bullet)
      if col:
        canvas.delete(bullet)
        bullets.pop(i)
        canvas.delete(inv)
        invs.pop(j)
        i -= 1
        j -= 1
        sizeB -= 1
        sizeI -= 1
        tot_cols += 1

      j += 1
    i += 1
  return tot_cols


def update(main,Dir,invs,bullets, counter, speed, score):

  global b_flag, canvas
  move_bullets(bullets)

  score += check_cols(bullets,invs)
  lost = 0
  if counter % 20 == 0:
    speed = speed - 30 if speed > 30 else 30

  if counter % 2 == 0:
    Dir,counter, lost = move_invs(Dir,invs, counter)
  if counter % 2 == 1:
    b_flag = 1

  if invs==[]:
    print("Victory!")
    restart(main, score)
  elif not lost:
    main.after(speed,update,main,Dir, invs,bullets, counter +1, speed, score)
  else:
    print("Lost!")
    restart(main, score)

def restart(main, score):
  main.destroy()
  print(score)
  game()


def move_player (event, player, bullets):  
  global b_flag, canvas
  if event.keysym=='Left':
    canvas.move(player,-10,0)
  elif event.keysym=='Right':
    canvas.move(player,10,0)
  elif event.keysym=='Up' and b_flag:
    cx1,cy1 = canvas.coords(player)
    bullets.append(canvas.create_rectangle(cx1-3,cy1-30,cx1+3,cy1-20, fill="yellow"))
    b_flag = 0


def game():
  global b_flag, canvas
  main = Tk()
  b_flag = 1
  main.geometry("400x600+100+100")
  canvas = Canvas(main,width=400, height = 600, bg="gray")
  canvas.pack()
  inv1_IMG = PhotoImage(file='inv1.png')
  player_IMG = PhotoImage(file='nave.png')

  player = canvas.create_image(200,570, image=player_IMG)

  Dir = -1
  invs = []
  bullets = []

  for i in range(5):
    for j in range(8):
      invs.append(canvas.create_image(j*31+35,i*25+11, image=inv1_IMG))

  update(main,Dir,invs, bullets, 0, 201, 0)

  main.bind('<Key>', lambda e: move_player(e,player, bullets)) 
  main.mainloop()


game()