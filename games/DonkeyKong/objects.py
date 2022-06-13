import tkinter as tk
import constants

class Mario:
    def __init__(
        self,
        map_canvas: tk.Canvas,
        paddle_list: list['Paddle'],
        stair_list : list['Stair'],
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ):
        self.id_: tk._CanvasItemId = map_canvas.create_oval(x1, y1, x2, y2, fill="#eb3737")
        self.map_canvas: tk.Canvas = map_canvas
        self.stair_list = stair_list
        self.paddle_list = paddle_list
        self.x = x1
        self.y = y1
        self.x2 = x2
        self.y2 = y2
        self.current_paddle: int = 0
        self.speed: int = 10
        self.jumping = 0
        self.jump_counter = 0
        self.JUMP_LIMIT = 5
        self.moving = 0

    def go_left(self, event):
        self.moving = 1

    def go_right(self, event):
        self.moving = 2

    def stop_moving(self, event):
        self.moving = 0

    def left(self) -> None:
        if (not self.in_stair() or self.jumping) and (self.x >= self.speed):
            if (self.x >= (self.paddle_list[self.current_paddle].x + self.speed)):
                self.map_canvas.move(self.id_, -1 * self.speed, 0)
                self.x -= self.speed
                self.x2 -= self.speed
        return

    def right(self) -> None:
        if (not self.in_stair() or self.jumping) and (self.x2 <= (constants.WIDTH - self.speed)):
            if (self.x2 <= (self.paddle_list[self.current_paddle].x2 - self.speed)):
                self.map_canvas.move(self.id_, self.speed, 0)
                self.x += self.speed
                self.x2 += self.speed
        return

    def update(self):

        if self.moving == 1:
            self.left()
        if self.moving == 2:
            self.right()


        if self.jumping != 0:
            if (self.jumping == 1) and (self.jump_counter == self.JUMP_LIMIT):
                self.jumping = 2
            if (self.jumping == 2) and (self.jump_counter == 0):
                self.jumping = 0
            
            if self.jumping == 1:
                self.jump_counter += 1
                self.y -= self.speed
                self.y2 -= self.speed
                self.map_canvas.move(self.id_, 0, -self.speed)

            if self.jumping == 2:
                self.jump_counter -= 1
                self.y += self.speed
                self.y2 += self.speed
                self.map_canvas.move(self.id_, 0, self.speed)




    def get_current_paddle(self):
        for i, paddle in enumerate(self.paddle_list):
            if paddle.y == self.y2:
                return i
        return -1


    def up(self, event) -> None:
        #print("climbing")
        for stair_ in self.stair_list:
            if (stair_.x < self.x) and (stair_.x2 > self.x2) and ((stair_.y - 10) < self.y2) and (stair_.y2 >= self.y2):
                self.map_canvas.move(self.id_, 0, -self.speed)
                self.y -= self.speed
                self.y2 -= self.speed
        self.current_paddle = self.get_current_paddle()        
        return

    def in_stair(self) -> bool:
        for stair_ in self.stair_list:
            if (stair_.x < self.x) and (stair_.x2 > self.x2) and ((stair_.y -10) < self.y2) and ((stair_.y2 - 10) >= self.y2):
                return True
        return False

    def down(self, event) -> None:
        #print("climbing")
        for stair_ in self.stair_list:
            if (stair_.x < self.x) and (stair_.x2 > self.x2) and ((stair_.y - 20) < self.y2) and ((stair_.y2 - 10) >= self.y2):
                self.map_canvas.move(self.id_, 0, self.speed)
                self.y += self.speed
                self.y2 += self.speed
        
        self.current_paddle = self.get_current_paddle()
        return

    def jump(self, event) -> None:
        if self.jumping == 0:
            self.jumping = 1

        return



class Paddle:
    def __init__(
        self, canvas: tk.Canvas, x: int, y: int, w: int, h: int, color="#7D0964"
    ):
        self.x : int = x
        self.y : int = y
        self.w : int = w
        self.h : int = h
        self.x2 = x + w
        self.y2 = y + h
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
        self.y2 = y + h
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
        self.y2 = y + h
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
