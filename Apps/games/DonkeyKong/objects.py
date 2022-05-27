import tkinter as tk
import constants

class Mario:
    def __init__(
        self,
        map_canvas: tk.Canvas,
        paddle_list: list['Paddle'],
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ):
        self.id_: tk._CanvasItemId = map_canvas.create_oval(x1, y1, x2, y2, fill="#eb3737")
        self.map_canvas: tk.Canvas = map_canvas

        self.current_paddle: int = 0
        self.speed: int = 10

    def left(self, event) -> None:
        self.map_canvas.move(self.id_, -1 * self.speed, 0)
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


class Paddle:
    def __init__(
        self, canvas: tk.Canvas, x: int, y: int, w: int, h: int, color="#7D0964"
    ):
        self.x : int = x
        self.y : int = y
        self.w : int = w
        self.h : int = h
        self.x2 = x + w
        self.id_ : tk._CanvasItemId = canvas.create_rectangle(x, y, x + w, y + h, fill=color)


class Stair:
    def __init__(
        self, canvas: tk.Canvas, x: int, y: int, w: int, h: int, color="#097D77"
    ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x2 = x + w
        self.id_  : tk._CanvasItemId = canvas.create_rectangle(x, y, x + w, y + h, fill=color)


class Barrel:
    def __init__(
        self, canvas : tk.Canvas, x:int, y:int, paddle_list : list[Paddle], w : int = 10, h : int = 10
    ):
        self.current_paddle : int = -len(paddle_list)        
        self.vx : int = 10
        self.vy : int = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.falling = False
        self.x2 = x + w
        self.id_ : tk._CanvasItemId = canvas.create_oval(x, y, x+w, y+h )

    def update(self, canvas : tk.Canvas, paddle_list : list[Paddle]) -> int:

        self.x += self.vx
        self.y += self.vy

        tk.Canvas.move(canvas, self.id_, self.vx, self.vy)

        if self.x >= constants.WIDTH or self.x <= 0:
            self.vy *= -1
            if self.current_paddle == 0:
                return 1

        if self.x >= paddle_list[self.current_paddle].x2 or self.x <= paddle_list[self.current_paddle].x:
            self.falling = True

        if self.falling and self.y >= (paddle_list[self.current_paddle + 1].y):
            self.falling = False

            
        return 0
