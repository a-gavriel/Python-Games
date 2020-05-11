from tkinter import *
from random import randint 
from numpy import random
from numpy import uint32
Width = 400
Height = 600
Difficulty = 4
Score = 0

class Block():
  def __init__(self):
    self.mat = random.randint(2,size=(Difficulty,Difficulty))
    self.tiles = []
    self.scale = 20
    self.speed = 10
    self.build_block()

  def build_block(self):
    global canvas
    y = 100  
    for row in self.mat:
      x = 140
      for e in row:
        if e:
          newTile = canvas.create_rectangle(x,y,x+self.scale,y+self.scale,fill="grey")
          self.tiles.append(newTile)
        x += self.scale
      y += self.scale

  def newblock(self):
    self.mat = random.randint(2,size=(Difficulty,Difficulty))
    self.tiles = []
    self.build_block()

  def move_block(self):
    global canvas, Height    
    for tile in self.tiles:    
      canvas.move(tile,0,self.speed)
      _,y1,_,_ = canvas.coords(tile)
      if y1+self.speed == Height:
        return 1
    return 0

def shoot():
  global shooting
  shooting = True
  
def new_shot():
  global player, canvas, shoots
  x1,y1,x2,_ = canvas.coords(player)
  sh = 14
  sw = 4
  sx = (x2-x1)//2 + x1 - sw//2
  sy = y1 - sh
  newShot = canvas.create_rectangle(sx,sy,sx+sw,sy+sh, fill = "#fcba03", outline = "#fcba03" )
  shoots.append(newShot)

def collision(rect1, rect2):
  x1,y1,x2,y2 = rect1
  sx,sy,_,_ = rect2
  if x1 <= sx and sx <=x2:
    if y1 <= sy and sy <= y2:
      return True
  else:
    return False

def move_shots(block):
  global shoots, canvas, Score
  j = 0
  n_shots = len(shoots)
  while j < n_shots:
    shot = shoots[j]
    canvas.move(shot,0,-10)
    sc = canvas.coords(shot)
    if sc[3] < 0: # out of screen
      shoots.pop(j)
      n_shots = len(shoots)
      j -= 1
    for i in range(len(block.tiles)):
      tile = block.tiles[i]
      tc = canvas.coords(tile) 
      if collision(tc,sc):
        Score += 1
        canvas.delete(tile)
        block.tiles.pop(i)
        canvas.delete(shot)
        shoots.pop(j)
        n_shots = len(shoots)
        j -= 1
        if len(block.tiles) == 0:
          Score += 2
          print("Destroyed!")
          block.newblock()
        break
    j += 1

def update(counter, block):
  global main, player, shooting
  lost = 0
  if counter % 4 == 0:
    if shooting:
      new_shot()
      shooting = False
  if counter % 2:
    lost = block.move_block()
    move_shots(block)
  if lost:
    print(Score)
    restart()
  if counter == 2**20:
    counter = -1
  main.after(100,update,counter+1, block)

def run():
  global main, canvas, shoots, shooting, player
  shooting = False
  main = Tk()
  main.geometry(str(Width)+"x"+str(Height)+"+200+200")
  main.resizable(width=False, height=False)
  main.focus_force()
  canvas = Canvas(main,width = Width,height= Height)
  canvas.pack()
  player = canvas.create_rectangle(180,580,200,600,fill="green")
  block = Block()
  shoots = []
  main.bind('<KeyRelease-Up>', lambda e: shoot())
  main.bind('<Left>', lambda e: canvas.move(player,-20,0))
  main.bind('<Right>', lambda e: canvas.move(player,20,0))
  update(uint32(0), block)
  main.mainloop()

def restart():
  global main
  main.destroy()
  run()

run()