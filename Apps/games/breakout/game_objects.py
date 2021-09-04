import pygame
from constants import *
from random import randint
from physics import *


class GameObject():
  """
  Basic Game Object with a rectangle, render and move function
  
  """
  def __init__(self):
    self.Rect = pygame.rect.Rect((10,10,10,10))
  def render(self, gameDisplay):
    pygame.draw.rect(gameDisplay,(0,0,0),self.Rect )
  def move(self,dx,dy):
    self.Rect = self.Rect.move(dx,dy)

class Player(GameObject):
  """
  Player Game Object, it can move!
  
  """
  def __init__(self):
    super().__init__()
    self.Rect = pygame.rect.Rect((GAME_WIDTH//2-50,(7*GAME_HEIGHT)//8,100,10))
  def move(self,dx,dy):    
    self.Rect = self.Rect.move(dx,0)
    new_x_left, new_x_right = self.Rect.left, self.Rect.right
    if self.Rect.left < 0:
      self.Rect = self.Rect.move( 0 - new_x_left, 0 )
    if self.Rect.right > GAME_WIDTH:
      self.Rect = self.Rect.move( (GAME_WIDTH) - new_x_right, 0 )



class Ball(GameObject):
  """
  Ball Game Object, can bounce. Starts without moving.
  """
  def __init__(self):
    super().__init__()
    self.img = pygame.image.load("ball-2.png").convert_alpha()
    self.Rect = self.img.get_rect()
    self.spawn()
    self.speed_x = 0
    self.speed_y = 0
    self.MAX_SPEED = 15

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
    self.Rect = self.Rect.move( spawn_x - self.Rect.left , spawn_y-self.Rect.top )

  def update(self):
    self.Rect = self.Rect.move(self.speed_x,self.speed_y)
    if self.Rect.left < 0 or self.Rect.right > GAME_WIDTH:
      self.speed_x = -self.speed_x
    if self.Rect.top < 0:
      self.speed_y = -self.speed_y
    
    if self.Rect.top > GAME_HEIGHT:
      return True
    else:
      return False

  def render(self,gameDisplay):
    gameDisplay.blit(self.img, self.Rect)


class Brick(GameObject):
  
  def __init__(self):
    super().__init__()  
    self.img = pygame.image.load("brick.png").convert()
    self.Rect = self.img.get_rect()
  def render(self,gameDisplay):
    gameDisplay.blit(self.img, self.Rect)