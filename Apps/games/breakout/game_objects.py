import pygame
from constants import *
from random import randint
from physics import *


class GameObject():
  def __init__(self,game):
    self.width = 10
    self.height = 10
    self.xpos = GAME_WIDTH // 2
    self.ypos = GAME_HEIGHT // 10    
    self.rect = pygame.rect.Rect(( self.xpos - self.width//2 , self.ypos - self.height//2 , self.width, self.height))   
  def left(self):
    return self.xpos - self.width//2
  def right(self):
    return self.xpos + self.width//2
  def top(self):
    return self.ypos - self.height//2
  def bottom(self):
    return self.ypos + self.height//2
  def get_xpos(self):
    return self.xpos
  def get_ypos(self):
    return self.ypos
  def get_rect(self):
    return pygame.rect.Rect(( self.xpos - self.width//2 , self.ypos - self.height//2 , self.width, self.height))   
  def update(self):
    None
  def render(self, game):    
    pygame.draw.rect(game.gameDisplay,(0,0,0), self.get_rect() )



# TODO: verify speed
class Player(GameObject):
  def __init__(self,game):
    super().__init__(game)   
    self.xspeed = 20 
    self.xpos = 200
    self.width = 500    
    self.ypos = 450
  def update(self,direction):
    if direction == 1:
      if self.left() > 0:
        self.xpos-= self.xspeed
    if direction == 2:
      if self.right() < GAME_WIDTH:
        self.xpos += self.xspeed
    self.rect = pygame.rect.Rect(( self.xpos - self.width//2 , self.ypos - self.height//2 , self.width, self.height))  

# TODO: verify speed
class Ball(GameObject):
  def __init__(self,game):
    super().__init__(game)
    self.basespeed = GAME_SPEED
    self.xspeed = self.basespeed
    self.yspeed = self.basespeed
    self.width = 7
    self.height = 7    
    self.xpos = randint(100,500)
    self.ypos = GAME_WIDTH//3
    self.pong = pygame.mixer.Sound('Blip_1-Surround-147.wav')
    self.pong.set_volume(10)    

  def update(self, game, player):
    self.rect = pygame.rect.Rect(( self.xpos - self.width//2 , self.ypos - self.height//2 , self.width, self.height))  
    self.xpos += (self.xspeed )
    self.ypos += (self.yspeed )
    if (self.xpos <= 0):
      self.xspeed *= -1
    if (self.xpos >= GAME_WIDTH):
      self.xspeed *= -1
    if (self.ypos <= 0):
      self.yspeed *= -1
    if (self.ypos > GAME_HEIGHT):
      game.crash = True
    col_result = colission(self,player)
    #print(self.xpos, self.ypos)
    if col_result[0]:      
      self.yspeed *= -1
      print(col_result[1])


class Brick(GameObject):
  def __init__(self):
    super().__init__(self)  
    self.xpos = 0
    self.ypos = 0    
    self.width = 52
    self.height = 21
    