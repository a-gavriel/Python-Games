import tkinter
from tkinter import*
import random
from itertools import permutations 


perms = [i for i in permutations((i for i in range(150,401,50)), 2) ]


def motion(event):
    x, y = event.x, event.y
    x1, y1, x2, y2 = canvas.coords(r1)
    if ((x1 -9)< x < (x2+9) and (y1-9)<y<(y2+9)):
      nx, ny = random.choice(perms)
      canvas.move(r1,nx-x,ny-y)
      canvas.move(r2,nx-x,ny-y)
      
      


root = Tk()
canvas = Canvas(root, bg ="#108010",width = 512,height =512)
canvas.pack()

t = Label(root, text="¿Bryan jugará Terraria?", font=("Helvetica", 20))
t.place(x=120,y=50)

r3 = canvas.create_rectangle(300,300,400,350, fill= "white", outline = "grey")
r4 = canvas.create_text(350,325,  text="NO", font=("Helvetica", 15))

r1 = canvas.create_rectangle(100,300,200,350, fill= "white", outline = "grey", activefill="pink")
r2 = canvas.create_text(150,325,  text="SÍ", font=("Helvetica", 15))




root.bind('<Motion>', motion)
root.mainloop()
