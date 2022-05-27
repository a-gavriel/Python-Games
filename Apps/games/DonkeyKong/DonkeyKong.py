import tkinter as tk
from constants import *
from objects import Mario, Paddle, Stair, Barrel




def create_paddles(canvas : tk.Canvas) -> list[Paddle]:
  paddle_list = [
    Paddle(canvas, *PADDLE_1_COORDS),
    Paddle(canvas, *PADDLE_2_COORDS),
    Paddle(canvas, *PADDLE_3_COORDS),
    Paddle(canvas, *PADDLE_4_COORDS),
    Paddle(canvas, *PADDLE_5_COORDS),
  ]

  return paddle_list

def create_stairs(canvas : tk.Canvas) -> list[Stair]:
  stair_list = [
    Stair(canvas, *STAIR_1_COORDS),
    Stair(canvas, *STAIR_2_COORDS),
    Stair(canvas, *STAIR_3_COORDS),
    Stair(canvas, *STAIR_4_COORDS)
  ]

  return stair_list


def update_all(main_window : tk.Tk, player : Mario,  paddle_list : list[Paddle], counter : int = 0):

  #barrel.update( canvas , paddle_list )

  if counter % 3 == 0:
    player.update()

  
  main_window.after(5, update_all, main_window, player, paddle_list, counter + 1)


def main():
  main_window = tk.Tk()
  main_window.geometry(str(WIDTH)+"x"+str(HEIGHT)+"+200+200")
  main_window.resizable(width = False, height = False)
  main_window.focus_force()
  canvas = tk.Canvas(main_window, width = WIDTH, height = HEIGHT)    
  canvas.pack()


  paddle_list : list[Paddle] = create_paddles(canvas)
  stair_list : list[Stair] = create_stairs(canvas)
  

  player = Mario(canvas, paddle_list, stair_list, 50, MARIO_Y1, 70, PADDLE_1_Y1)
  barrel = Barrel(canvas, 20, 90, paddle_list)

  update_all(main_window, player, paddle_list)

  main_window.bind("<KeyPress-Left>", player.go_left)
  main_window.bind("<KeyPress-Right>", player.go_right)
  main_window.bind("<KeyRelease-Left>", player.stop_moving)
  main_window.bind("<KeyRelease-Right>", player.stop_moving)
  
  main_window.bind("<KeyPress-Up>", player.up)
  main_window.bind("<KeyPress-Down>", player.down)
  main_window.bind("<space>", player.jump)

  main_window.mainloop()

if __name__ == "__main__":
  main()