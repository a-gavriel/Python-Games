import tkinter as tk
from constants import *
from objects import Mario



def main():
  main_window = tk.Tk()
  main_window.geometry(str(WIDTH)+"x"+str(HEIGHT)+"+200+200")
  main_window.resizable(width = False, height = False)
  main_window.focus_force()
  canvas = tk.Canvas(main_window, width = WIDTH, height = HEIGHT)    
  canvas.pack()


  paddle_list = [
    canvas.create_rectangle(*PADDLE_1_COORDS, fill="#7d0964"),
    canvas.create_rectangle(*PADDLE_2_COORDS, fill="#7d0964"),
    canvas.create_rectangle(*PADDLE_3_COORDS, fill="#7d0964"),
    canvas.create_rectangle(*PADDLE_4_COORDS, fill="#7d0964"),
    canvas.create_rectangle(*PADDLE_5_COORDS, fill="#7d0964"),
  ]

  player = Mario(canvas, paddle_list, 50, MARIO_Y1, 70, PADDLE_1_Y1)
  
  main_window.bind("<KeyPress-Left>", player.left)
  main_window.bind("<KeyPress-Right>", player.right)
  main_window.bind("<KeyPress-Up>", player.up)
  main_window.bind("<space>", player.jump)

  main_window.mainloop()

if __name__ == "__main__":
  main()