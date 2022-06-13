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


def update_all(main_window : tk.Tk, player : Mario,  paddle_list : list[Paddle], \
              barrel_list : list[Barrel], counter : int = 0):

  if counter % 5 == 0:
    for barrel in barrel_list:
      barrel.update(paddle_list)

  if counter % 3 == 0:
    player.update()

  
  main_window.after(5, update_all, main_window, player, paddle_list, barrel_list, counter + 1)


def main():
  main_window = tk.Tk()
  main_window.geometry(str(WIDTH)+"x"+str(HEIGHT)+"+100+100")
  main_window.resizable(width = False, height = False)
  main_window.focus_force()
  canvas = tk.Canvas(main_window, width = WIDTH, height = HEIGHT)    
  canvas.pack()


  paddle_list : list[Paddle] = create_paddles(canvas)
  stair_list : list[Stair] = create_stairs(canvas)
  barrel_list : list[Barrel] = []

  player = Mario(canvas, paddle_list, stair_list, 50, MARIO_Y1, 70, PADDLE_1_Y1)
  
  barrel_list.append(Barrel(canvas, 20, 90, paddle_list))

  update_all(main_window, player, paddle_list, barrel_list)

  main_window.bind("<KeyPress-Left>", player.manage_keys)
  main_window.bind("<KeyRelease-Left>", player.manage_keys)

  main_window.bind("<KeyPress-Right>", player.manage_keys)
  main_window.bind("<KeyRelease-Right>", player.manage_keys)

  main_window.bind("<KeyPress-Up>", player.manage_keys)
  main_window.bind("<KeyRelease-Up>", player.manage_keys)
  
  main_window.bind("<KeyPress-Down>", player.manage_keys)
  main_window.bind("<KeyRelease-Down>", player.manage_keys)

  main_window.bind("<space>", player.jump)

  main_window.mainloop()

if __name__ == "__main__":
  main()