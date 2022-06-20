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
        self.lives = 3
        self.x = x1
        self.y = y1
        self.x2 = x2
        self.y2 = y2
        self.current_paddle: int = 0
        self.speed: int = 5
        self.jumping = 0
        self.jump_counter = 0
        self.JUMP_LIMIT = 5
        self.moving = 0
        self.pressed_keys = {
            "LEFT" : False,
            "RIGHT" : False,
            "UP" : False,
            "DOWN" : False
        }

    def manage_keys(self, event):
        pressed = event.type == '2'
        released = event.type == '3'
        key_pressed = event.keysym.upper()

        if key_pressed == 'RIGHT':
            if pressed: 
                self.pressed_keys['RIGHT'] = True
            elif released:
                self.pressed_keys['RIGHT'] = False
                
        if key_pressed == 'LEFT':
            if pressed: 
                self.pressed_keys['LEFT'] = True
            elif released:
                self.pressed_keys['LEFT'] = False

        if key_pressed == 'UP':
            if pressed: 
                self.pressed_keys['UP'] = True
            elif released:
                self.pressed_keys['UP'] = False

        if key_pressed == 'DOWN':
            if pressed: 
                self.pressed_keys['DOWN'] = True
            elif released:
                self.pressed_keys['DOWN'] = False


        return 
        



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

        if self.pressed_keys['LEFT'] and not self.pressed_keys['RIGHT']:
            self.left()
        
        if self.pressed_keys['RIGHT'] and not self.pressed_keys['LEFT']:
            self.right()
        
        if self.pressed_keys['UP'] and not self.pressed_keys['DOWN']:
            self.up()
        
        if self.pressed_keys['DOWN'] and not self.pressed_keys['UP']:
            self.down()

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

        return


    def get_current_paddle(self):
        for i, paddle in enumerate(self.paddle_list):
            if paddle.y == self.y2:
                return i
        return -1

    def in_stair(self) -> bool:
        for stair_ in self.stair_list:
            if (stair_.x < self.x) and (stair_.x2 > self.x2) and ((stair_.y - self.speed) < self.y2) and ((stair_.y2 - self.speed) >= self.y2):
                return True
        return False

    def up(self) -> None:
        if self.jumping > 0:
            return
            
        for stair_ in self.stair_list:
            if (stair_.x < self.x) and (stair_.x2 > self.x2) and ((stair_.y - self.speed) <= self.y2) and (stair_.y2 >= self.y2):
                self.map_canvas.move(self.id_, 0, -self.speed)
                self.y -= self.speed
                self.y2 -= self.speed
        self.current_paddle = self.get_current_paddle()        
        return


    def down(self) -> None:
        if self.jumping > 0:
            return

        for stair_ in self.stair_list:
            if (stair_.x < self.x) and (stair_.x2 > self.x2) and ((stair_.y - (2*self.speed)) <= self.y2) and ((stair_.y2 - self.speed) >= self.y2):
                self.map_canvas.move(self.id_, 0, self.speed)
                self.y += self.speed
                self.y2 += self.speed
        
        self.current_paddle = self.get_current_paddle()
        return

    def jump(self, event) -> None:
        if (self.jumping == 0) and not (self.in_stair()):
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
        self, canvas : tk.Canvas, x:int, y:int, paddle_list : list[Paddle], w : int = 15, h : int = 15
    ):
        self.number_of_falls : int = 0
        self.map_canvas : tk.Canvas = canvas
        self.vx : int = 10
        self.vy : int = 10
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.falling = False
        self.x2 = x + w
        self.y2 = y + h
        self.id_ : tk._CanvasItemId = canvas.create_oval(x, y, x+w, y+h )


    def update(self, paddle_list : list[Paddle]) -> int:

        self.x += self.vx
        self.x2 += self.vx
        tk.Canvas.move(self.map_canvas, self.id_, self.vx, 0)

        flipped_direction : bool = False

        if self.falling:
            self.y += self.vy
            self.y2 += self.vy
            tk.Canvas.move(self.map_canvas, self.id_, 0, self.vy)


        current_paddle : int = self.get_current_paddle(paddle_list)

        if self.x >= constants.WIDTH or self.x <= 0:
            self.vx *= -1
            self.x += self.vx
            self.x2 += self.vx
            tk.Canvas.move(self.map_canvas, self.id_, self.vx, 0)
            flipped_direction = True
            self.number_of_falls += 1
            if (current_paddle == 0) and (self.number_of_falls == len(paddle_list)):
                return 1
        
        if (current_paddle >= 0) or ((self.falling) and (self.y >= (paddle_list[current_paddle + 1].y))):
            self.falling = False

        if (not self.falling) and (current_paddle == -1) and not (flipped_direction):
            self.falling = True
        
        
        if (not self.falling) and ((self.x >= paddle_list[current_paddle].x2) or (self.x2 <= paddle_list[current_paddle].x)):
            self.falling = True


        
        return 0


    def get_current_paddle(self, paddle_list : list[Paddle]) -> int:
        for i, paddle in enumerate(paddle_list):
            if paddle.y == self.y2:
                return i
        return -1