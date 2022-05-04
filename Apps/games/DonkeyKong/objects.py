import tkinter as tk


class Mario:
  def __init__(self, map_canvas : tk.Canvas, paddle_list : list, 
      x1 : int, y1 : int, x2 : int, y2 : int):
    self.id_ : int = map_canvas.create_oval(x1, y1, x2, y2, fill = "#eb3737")
    self.map_canvas : tk.Canvas = map_canvas
    

    self.current_paddle : int = 0
    self.speed = 10

  def left(self, event) -> None:
    self.map_canvas.move(self.id_, -1*self.speed, 0)
    return

  def right(self, event) -> None:
    self.map_canvas.move(self.id_, self.speed, 0)
    return

  def up(self, event) -> None:
    print("climbing")
    return

  def jump(self, event) -> None:
    print("jumping")
    return

  def check_sides(self) -> bool:
    pass