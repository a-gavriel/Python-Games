import sys, pygame, random
from random import *
gamespeed = 1

sign = lambda x: (1, -1)[x < 0]

class GameObject():
  def __init__(self,scale, i = 1, j = 1):
    self.scale = scale
    self.i = i
    self.j = j    
    self.rect = pygame.rect.Rect(( self.j * self.scale , self.i * self.scale,  self.scale,  self.scale))     
  def update(self):
    None
  def render(self, game):
    self.rect = pygame.rect.Rect(( self.j * self.scale , self.i * self.scale,  self.scale,  self.scale))  
    
    pygame.draw.rect(game.gameDisplay,(0,0,0), self.rect )



# TODO: verify speed
class Player(GameObject):
  def __init__(self,scale, i = 1, j = 1, number = 1):
    super().__init__(scale, i , j)  
    self.dir_ = 0    
    self.alive = 1
    self.number = number
  def change_dir(self, new_dir):
    self.dir_ = new_dir
  def update(self, imax, jmax, mat):  
    if self.dir_ == 1:      
      self.j -= 1            
    if self.dir_ == 2:
      self.j += 1
    if self.dir_ == 3:
      self.i -= 1
    if self.dir_ == 4:
      self.i += 1

    out_map = self.j == -1 or self.j == jmax or self.i == -1 or self.i == imax
    if out_map:
      return 1
    else:

      collide = 0

      if mat[self.i][self.j] and self.dir_:      
        collide = 1


      if not collide:
        mat[self.i][self.j] = self.number
      return collide






class Game:
  def __init__(self,game_width,game_height):
    self.crash = False
    self.score =  0
    self.game_height = game_height
    self.game_width = game_width
    self.gameDisplay = pygame.display.set_mode((game_width,game_height+60))
    self.scale = 10
    self.size = (int(game_height/self.scale), int(game_width/self.scale))
    self.mat = [[0]*self.size[0] for i in range(self.size[1])]    
    self.player = Player(self.scale, 1, 1, 1)
        
    self.dic = {0:(255,255,255),
                1:(255,0,0),
                2:(0,255,0)}

  def update(self):
    self.crash = self.player.update(* self.size, self.mat)    

    #self.ball.update(self, self.player)
  def render(self):
    self.gameDisplay.fill((0,255,255))

    for i,row in enumerate(self.mat):
      for j,e in enumerate(row):
        rect = pygame.rect.Rect(( j * self.scale , i * self.scale,  self.scale,  self.scale))         
        pygame.draw.rect(self.gameDisplay, self.dic[ e ] , rect )

    self.player.render(self)
    pygame.display.flip()
    


def run():
  pygame.init()            
  clock = pygame.time.Clock()
  
  game = Game(400,400)
  #initializegame
  #render game
  final_move = 0
  p2_ = 0
  while(not game.crash):    

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_LEFT]:
      final_move = 1
    if pressed[pygame.K_RIGHT]:
      final_move = 2
    if pressed[pygame.K_UP]:
      final_move = 3
    if pressed[pygame.K_DOWN]:
      final_move = 4

    if pressed[pygame.K_a]:
      p2_ = 1
    if pressed[pygame.K_d]:
      p2_ = 2
    if pressed[pygame.K_w]:
      p2_ = 3
    if pressed[pygame.K_s]:
      p2_ = 4


        
    game.player.change_dir(final_move)   
    
    game.update()
    game.render()
    
    events = pygame.event.get()      
    for event in events:
      if event.type == pygame.QUIT:
        game.crash = True

    clock.tick(10)
    #render game
  pygame.quit()
  print("game finished!")
  

run()
