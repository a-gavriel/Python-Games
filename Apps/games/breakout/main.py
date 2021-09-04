
import sys, pygame, random
from random import *
from game_objects import *
from constants import *
from physics import *




class Game:
  def __init__(self,game_width,game_height):
    self.crash = False
    self.player = Player(self)
    self.ball = Ball(self)
    self.score =  0
    self.game_height = game_height
    self.game_width = game_width
    self.gameDisplay = pygame.display.set_mode((game_width,game_height+60))
    self.wall = Wall()
    self.wall.build_wall(GAME_WIDTH) #TODO: goes here?
  def update(self):
    self.ball.update(self, self.player)
    self.wall.update(self.ball,self)    
  def render(self):
    self.gameDisplay.fill((0,255,255))
    self.player.render(self)
    self.ball.render(self)
    self.wall.render(self)
    pygame.display.flip()
    





class Wall:
  def __init__(self):

    self.bricks = []
    self.colors = []
    self.brick = pygame.image.load("brick.png").convert()
    self.brickrect = self.brick.get_rect()
  def build_wall(self, width):        
    Wxpos = 0
    Wypos = 60
    adj = 0
    for i in range (0, 14):        
      newbrick = Brick()
      newcolor = (randint(0,255),randint(0,255),randint(0,255))
      if Wxpos > width:
        if adj == 0:
          adj = newbrick.width // 2
        else:
          adj = 0
        Wxpos = -adj
        Wypos += newbrick.height      
      self.bricks.append(newbrick.get_rect())
      self.colors.append(newcolor)
      self.bricks[i] = self.bricks[i].move(Wxpos, Wypos)
      Wxpos = Wxpos + newbrick.width
  def update(self,ball, game):
    index = ball.rect.collidelist(self.bricks)       
    if index != -1: 
      if ball.rect.center[0] > self.bricks[index].right or \
        ball.rect.center[0] < self.bricks[index].left:
        ball.xspeed = -ball.xspeed
      else:
        ball.yspeed = -(ball.yspeed)
      ball.pong.play(0)              
      self.bricks[index:index + 1] = []
      self.colors[index:index + 1] = []
      game.score += 10
  def render(self,game):
    for i in range(len(self.bricks)):
    	game.gameDisplay.blit(self.brick, self.bricks[i])    
    	#pygame.Surface.blit(self.image, game.gameDisplay, self.bricks[i])
      #pygame.draw.rect(game.gameDisplay,self.colors[i],self.bricks[i])
      


def run():
  pygame.init()            
  counter_games = 0
  #create agent
  max_iterations = 10 #TODO: move to top
  clock = pygame.time.Clock()
  while counter_games < max_iterations:
    game = Game(640,480)
    #initializegame
    #render game
    while(not game.crash):
      #agent stuff
      final_move = 0 #default move

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_LEFT]:
        final_move = 1
      if pressed[pygame.K_RIGHT]:
        final_move = 2
      #final_move = randint(1,2) #TODO: replace with agent stuff


      game.player.update(final_move)     
      game.update()
      game.render()
      #print(game.ball.ypos)
      clock.tick(GAME_FPS)
      #render game
    print("game finished!")
    counter_games += 1

run()
