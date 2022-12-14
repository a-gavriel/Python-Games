import tkinter as tk
from constants import *
from objects import Mario, Paddle, Stair, Barrel
from random import random as random_f



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


def check_colisions(player : Mario, barrel_list : list[Barrel]) -> int:

  for i, barrel in enumerate(barrel_list):
    if ((barrel.x2 > player.x) and (barrel.x < player.x2) and (barrel.y < player.y2) and (barrel.y2 > player.y)):
      return i

  return -1

def update_all(main_window : tk.Tk, main_canvas : tk.Canvas, player : Mario,  \
              paddle_list : list[Paddle], barrel_list : list[Barrel], counter : int = 0):


  keep_playing = True

  if counter % 5 == 0:
    for i, barrel in enumerate(barrel_list):
      if barrel.update(paddle_list):
        main_canvas.delete(barrel.id_) #remove from canvas
        barrel_list.pop(i)  #remove from list
        break

      elif check_colisions(player, barrel_list) >= 0:
        print(f"Colision with Mario!, current lives: {player.lives-1}")
        main_canvas.delete(barrel.id_) #remove from canvas
        barrel_list.pop(i)  #remove from list
        player.lives -= 1
        keep_playing = (player.lives > 0)
        break

  if counter % 150 == 0:
    if random_f() > 0.5:
      barrel_list.append(Barrel(main_canvas, 20, 85, paddle_list))
  

  if counter % 3 == 0:
    player.update()

  if keep_playing:
    main_window.after(5, update_all, main_window, main_canvas, player, paddle_list, barrel_list, counter + 1)
  else:
    main_window.destroy() 





def game_handler():
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
  

  update_all(main_window, canvas, player, paddle_list, barrel_list)

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



def main():
  game_handler()

  return


if __name__ == "__main__":
  main()