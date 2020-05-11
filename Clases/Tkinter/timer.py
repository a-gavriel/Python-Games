"""
Original code: 

https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter

# for python 3.x use 'tkinter' rather than 'Tkinter'
import Tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()




"""
import tkinter as tk
import time

class Game:
  def __init__(self):
    self.counter = 0
  def update(self):
    global root
    print("updating...", self.counter)
    self.counter += 1
    #root.after(1000, self.update,)


def update_clock(game):
  global root
  now = time.strftime("%H:%M:%S")
  game.update()
  print("Updating and rendering", now)
  root.after(1000, update_clock, game)



def App():
    global root
    root = tk.Tk()
    label = tk.Label(text="")
    label.pack()
    g = Game()
    
    g.update()
    
    #update_clock(g)
    root.mainloop()

    

App()
