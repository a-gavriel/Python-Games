import pygame
from constants import *
from random import randint
from physics import *


class GameObject():
  """
  Basic Game Object with a rectangle, render and move function
  
  """
  def __init__(self, x = 0, y = 0, width = 10, height = 10):
    self._x = x
    self._y = y
    self._width = width
    self._height = height
    self.left = x
    self.top = y
    self.right = self.left + self.width
    self.bottom = self.top + self.height 
    self.coords = (self.left, self.top, self.right, self.bottom) 

  @property
  def width(self):
    return self._width
  @width.setter
  def width(self, val):
    self._width = val
    self.update_vars()

  @property
  def height(self):
    return self._height
  @height.setter
  def height(self, val):
    self._height = val
    self.update_vars()

  @property
  def x(self):
    return self._x
  @x.setter
  def x(self, val):
    self._x = val
    self.update_vars()

  @property
  def y(self):
    return self._y
  @y.setter
  def y(self, val):
    self._y = val
    self.update_vars()

  def update_vars(self):
    self.left = self.x
    self.top = self.y
    self.right = self.x + self.width
    self.bottom = self.y + self.height
    self.coords = (self.left, self.top, self.right, self.bottom) 

  def get_center(self):
    return self.left + (self.width/2) , self.top + (self.height/2)
    
  def move(self,dx,dy):
    self.x += dx
    self.y += dy
  
  def replace(self, x, y):
    self.x = x
    self.y = y

  def load_rect(self, render_rect):
    self.width = render_rect.width
    self.height = render_rect.height
    self.x = render_rect.left
    self.y = render_rect.top

  def get_render_rect(self):
    return pygame.rect.Rect((self.left,self.top,self.width,self.height))

  def render(self, gameDisplay):
    pygame.draw.rect(gameDisplay,(0,0,0), self.get_render_rect() )



class Player(GameObject):
  """
  Player Game Object, it can move!
  
  """
  def __init__(self):
    super().__init__(GAME_WIDTH//2-50,(7*GAME_HEIGHT)//8,100,10) 
    self.speedx = INITIAL_PLYR_SPEED
    self.speedy = 0   
  def update(self, action):    
    

    self.move(self.speedx * action,0)
    new_x_left, new_x_right = self.left, self.right
    if self.left < 0:
      self.move( 0 - new_x_left, 0 )
    if self.right > GAME_WIDTH:
      self.move( (GAME_WIDTH) - new_x_right, 0 )



class Ball(GameObject):
  """
  Ball Game Object, can bounce. Starts without moving.
  """
  def __init__(self):
    super().__init__()
    self.img = pygame.image.load("ball-2.png").convert_alpha()
    self.load_rect( self.img.get_rect() )
    self.spawn()
    self.speed_x = 0
    self.speed_y = 0
    self.MAX_SPEED = 0.5

  def start_ball(self):
    if (self.speed_x == 0) and (self.speed_y == 0):
      self.speed_x = 0
      self.speed_y = INITIAL_BALL_SPEED

  def spawn(self):
    self.speed_x = 0
    self.speed_y = 0
    spawn_range_x = (GAME_WIDTH//4,(GAME_WIDTH*3)//4)
    spawn_x = randint(*spawn_range_x)
    spawn_y = (GAME_HEIGHT)//3
    self.replace( spawn_x , spawn_y)

  def update(self):
    self.move(self.speed_x, self.speed_y)
    if self.left < 0 or self.right > GAME_WIDTH:
      self.speed_x = -self.speed_x
    if self.top < 0:
      self.speed_y = -self.speed_y
    
    if self.top > GAME_HEIGHT:
      return True
    else:
      return False

  def render(self,gameDisplay):
    gameDisplay.blit(self.img, self.get_render_rect())


class Brick(GameObject):
  
  def __init__(self, x, y, width, height, resistance = 1, color = (150,150,150)):
    super().__init__(x, y, width, height)  
    self.resistance = resistance
    self.color = color
