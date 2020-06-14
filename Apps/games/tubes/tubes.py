from tkinter import *
import random
from math import ceil
colors = ["blue", "red2", "snow", "green2", "green4", "orange", "purple1", "purple4", "pink1", "cyan", "slate gray" ]
color_codes = range(len(colors))


def circle(canvas,x,y, r, color):
   id = canvas.create_oval(x-r,y-r,x+r,y+r, fill=colors[color])
   return id

def check_hand(e,tubes, tubes_graph):#runs on mouse motion
  global canvas, selected
  tube_clic = None
  for i in range(len(tubes)):
    tube_ = tubes[i]    
    bbox= canvas.bbox(tube_.img)    
    if bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[3] > e.y:#checks whether the mouse is inside the boundrys
        tube_clic = i
        tube_.print()
  if tube_clic != None:
    selected.pop(1)
    selected.insert(0,tube_clic)
    print("clic: ",tube_clic, selected)
  else:
    selected[0] = None
  if selected[1] != None:
    if selected[0] != selected[1]:
      move_ball(tubes,selected[0],selected[1])
      selected = [None,None]
  vic = 1
  for t in tubes:
    c = t.check()
    vic = vic and c
  if vic == 1:
    print("VICTORY!!")
        
def move_ball(tubes,tubeindex1,tubeindex2):
  global selected
  lt1 = len(tubes[tubeindex1].balls) 
  lt2 = len(tubes[tubeindex2].balls)
  if lt1 == 5 or lt2 == 5:
    selected = [None,None]
  

  if lt1 > 0:
    bc_there = canvas.itemcget(tubes[tubeindex1].balls[-1],"fill")
    bc_here = canvas.itemcget(tubes[tubeindex2].balls[-1],"fill")
    if bc_there != bc_here:
      print("cant")
      return None

  ball2 = tubes[tubeindex2].balls.pop()
  tubes[tubeindex1].drop(ball2)


class Tube():
  def __init__(self,x,y,tube_img,num):
    self.x = x
    self.y = y
    self.img = canvas.create_image(x,y, image=tube_img)
    self.num = num
    self.balls = []
    self.filled = 0
    print(self.img)
  def print(self):    
    print("Tube info:",self.x,self.y,self.img,self.num,self.balls)
  def check(self):
    if self.balls == []:
      return 1
    if len(self.balls) == 4:
      r = 1
      c = canvas.itemcget(self.balls[0],"fill")
      for ball in self.balls:
        bc_there = canvas.itemcget(ball,"fill")
        r = r and (c == bc_there)
        c = bc_there
      return r
    else:
      return 0
  def drop(self,ball):
    if len(self.balls) == 4:
      return None
    x1,y1,_,_ = canvas.coords(ball)
    bx,by = x1+11, y1+11
    tx,ty = self.x,0
    if len(self.balls) == 0:
      ty = self.y+23*2
    if len(self.balls) == 1:
      ty = self.y+15
    if len(self.balls) == 2:
      ty = self.y-15
    if len(self.balls) == 3:
      ty = self.y-23*2
    canvas.move(ball,tx-bx,ty-by)
    self.balls.append(ball)
    self.print()
    print("---------")

def graph_tubes(tot_tubes,tubes, pile, tube_img):
  global canvas
  
  diff = tot_tubes -2
  c_tube = 0
  print(tot_tubes,diff, len(pile)/4)
  for j in range(2):
    for i in range(ceil(tot_tubes/2)):
      if c_tube == tot_tubes:
        break
      tubes.append(Tube(i*60+27,j*150+80, tube_img, c_tube))
      if c_tube < diff:
        ballcolor = pile.pop()
        ball = (circle(canvas,i*60+27,j*150+80-23*2, 11, ballcolor) )
        tubes[c_tube].drop(ball)
        ballcolor = pile.pop()
        ball = (circle(canvas,i*60+27,j*150+80-15, 11, ballcolor) )
        tubes[c_tube].drop(ball)
        ballcolor = pile.pop()
        ball = (circle(canvas,i*60+27,j*150+80+15, 11, ballcolor) )
        tubes[c_tube].drop(ball)
        ballcolor = pile.pop()
        ball = (circle(canvas,i*60+27,j*150+80+23*2, 11, ballcolor) )
        tubes[c_tube].drop(ball)
      c_tube += 1


def game():  
  global canvas, selected
  random.seed(1)
  difficulty = 5
  selected = [None,None]
  tot_tubes = difficulty + 2  
  chosen_colors = random.sample(color_codes,difficulty)
  pile = 4 * chosen_colors
  tubes = []*tot_tubes


  random.shuffle(pile)

  main = Tk()
  tube_img = PhotoImage(file='tube.png')
  main.geometry(str(ceil(tot_tubes/2)*120)+"x300+100+100")
  canvas = Canvas(main,width = ceil(tot_tubes/2)*150,height = 300, bg = "white")
  canvas.pack()

  tubes_graph = []



  graph_tubes(tot_tubes,tubes,  pile, tube_img)



  canvas.bind("<Button-1>",lambda e:check_hand(e,tubes,tubes_graph ))#binding to motion
  main.mainloop()

game()