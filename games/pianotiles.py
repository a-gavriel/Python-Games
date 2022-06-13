from tkinter import *
from random import randint 

Difficulty = 4
Width = 400
Height = 600

class Key:
  def __init__(self, x, y, col , active=False):
    global canvas, Width, Difficulty
    self.x = x
    self.y = y
    self.col = col
    self.width = Width//Difficulty - 1
    self.height = 149
    self.active = active
    self.color = "black" if active else "white"
    self.rect = canvas.create_rectangle(x,y,x+self.width,y+self.height, fill= self.color, outline = "grey")    
  def move(self, activeKey):
    global canvas
    canvas.move(self.rect, 0,2)
    self.y += 2
    if self.y == 600:
      canvas.move(self.rect, 0, -150-self.y)
      self.y = -150
      if(activeKey == self.col):
        self.active = True
        self.color = "black" 
        canvas.itemconfig(self.rect, fill='black')
      else:
        self.active = False
        self.color = "white" 
        canvas.itemconfig(self.rect, fill='white')
      
def move_keys(Keys):
  global main, Crash
  for row in Keys:
    activeKey = randint(0,Difficulty-1)
    for key in row:
      key.move(activeKey)
  if Crash:
    reset_game()
  main.after(6,move_keys, Keys)

def create_grid(Keys):
  global Height, Width, Difficulty
  rows = 5
  ScaleY = Height//(rows-1)
  ScaleX = Width//Difficulty
  for i in range(-1,rows-1):
    row = []
    for j in range(Difficulty):      
      newKey = Key(j*ScaleX,i*ScaleY, j,False)      
      row.append(newKey)
    Keys.append(row)

def clic(state):
  global isClicked 
  isClicked = state

def check(event, Keys):
  global Score, Crash
  x,y = event.x, event.y
  if isClicked:
    for row in Keys:
      for key in row:
        if (key.x < x and x < key.x + key.width) and (key.y < y < key.y + key.height):
          if key.active == 1:
            key.active = 2
            Score += 1            
            canvas.itemconfig(key.rect, fill='cyan')
          elif key.active == 0:
            print(Score)
            Crash = True
          
def run():
    global  main, canvas, isClicked, Score, Crash
    Crash = False
    main = Tk()
    #update_clock()
    main.geometry(str(Width)+"x"+str(Height)+"+200+200")
    main.resizable(width=False, height=False)
    main.focus_force()
    isClicked = True
    Score = 0
    canvas = Canvas(main, width=400, height=600, bg="gray")
    canvas.pack()
    Keys = []
    create_grid(Keys)
    main.bind('<Button-1>', lambda e: check(e,Keys))
    move_keys(Keys)
    main.mainloop()

def reset_game():
  global main
  main.destroy()
  run()

run()
