from tkinter import *
import random
G = 0.5
def sign(x):
  if x == 0:
    return 0
  if x > 0:
    return 1
  else:
    return -1

class sq():
  def __init__(self,x,y,w,h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.c = canvas.create_rectangle(x,y,x+w,y+h,fill="red")
    self.vx = 0
    self.vy = 0
  def start(self):
    self.vx = random.choice([-3,3])
    self.vy = -5
  def check_borders(self):    
    if (self.x+self.w >= 300) or (self.x <= 0):
      self.vx *= -1
    if (self.y <= 0):
      self.vy *= -1

    elif (self.y+self.h >= 300):
      #self.y = 300
      _,y1,_,_ = canvas.coords(self.c)
      canvas.move(self.c,0,250-y1)
      self.y = 250
      nvy = -1*0.8 * (self.vy)  
      if nvy < -1*G:    
        self.vy = nvy
      else: 
        self.y = 250
        self.vy = 0

  def move(self):
    self.vy = (self.vy)+G
    self.y += self.vy
    self.check_borders()

    self.x += self.vx
    canvas.move(self.c,self.vx,self.vy)
    print(self.y+self.h , self.vy)
    #canvas.coords(sq)




def update(main,sq):

  sq.move()

  main.after(10,update,main,sq)



def game():
  global canvas
  main = Tk()
  main.geometry("300x300+100+100")
  canvas = Canvas(main,width=300,height=300)
  canvas.pack()

  s = sq(100,200,50,50)
  s.start()

  update(main,s)

  main.mainloop()

game()