
import sys, pygame, random
from random import *
from game_objects import *
from constants import *
from physics import *


pygame.init()

class Game:
  def __init__(self):
    self.clock = pygame.time.Clock()
    self.gameDisplay = pygame.display.set_mode(DISPLAY_SIZE)
    self.game_paused = 0
    pygame.mouse.set_visible(self.game_paused)       # turn off mouse pointer
    self.crash = False
    self.player = Player()
    self.ball = Ball()
    self.score =  0
    self.wall = Wall()

  def update(self):
    #self.ball.update(self, self.player)
    #self.wall.update(self.ball,self)   
    if Collide(self.ball, self.player):
      ball_player_collision(self.ball, self.player)
    

    collided_brick_i = collide_list(self.ball, self.wall.brick_list)
    if collided_brick_i != -1:
      ball_brick_collision(self.ball, self.wall.brick_list[collided_brick_i])
      self.wall.brick_list.pop(collided_brick_i)
    
    if self.ball.update():
      self.ball.spawn()

  
  def main(self):
    
    
    while(not self.crash):
      self.clock.tick(GAME_FPS*10)

      # process key presses
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              self.game_paused = 1 - self.game_paused
              pygame.mouse.set_visible(self.game_paused) 

      
      if not self.game_paused:
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:                        
            self.player.update(-1)  
        if keys[pygame.K_RIGHT]:                  
            self.player.update(1)
        if keys[pygame.K_SPACE]:
            self.ball.start_ball()

        self.update()
      
      self.render(self.game_paused)

  def render(self, game_paused):
    bg_color = ( 0x2F, 0x4F, 0x4F )
    self.gameDisplay.fill(bg_color) #clean display
    self.player.render(self.gameDisplay)
    self.ball.render(self.gameDisplay)
    self.wall.render(self.gameDisplay)

    if game_paused:
      grey_image = pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
      grey_image.set_alpha(100)
      self.gameDisplay.blit(grey_image, (0,0))

      msg = pygame.font.Font(None,70).render(" Game Paused ", True, (0,255,255), (155,155,155))
      msgrect = msg.get_rect()
      msgrect = msgrect.move(GAME_WIDTH / 2 - (msgrect.center[0]), GAME_HEIGHT / 3)
      self.gameDisplay.blit(msg, msgrect)


    #self.wall.render(self)
    pygame.display.flip()
    

class Wall:
  def __init__(self):
    self.img = pygame.image.load("brick-1.png").convert()
    self.brick_list = []
    self.brick_width = 32
    self.brick_height = 13
    self.create_bricks()


  def create_bricks(self):
    temp_matrix = [
      [1,0,0,0, 0,0,0,0, 0,1,1,0, 0,0,0,0, 0,0,0,1],
      [0,1,0,0, 0,0,0,0, 0,1,1,0, 0,0,0,0, 0,0,1,0],
      [0,0,1,0, 0,0,0,0, 0,1,1,0, 0,0,0,0, 0,1,0,0],
      [0,0,0,1, 0,0,0,0, 0,1,1,0, 0,0,0,0, 1,0,0,0],
      [0,0,0,0, 0,0,0,0, 0,1,1,0, 0,0,0,0, 0,0,0,0]
    ]
    for i,row in enumerate(temp_matrix):
      for j,e in enumerate(row):
        if e != 0:
          #temp_rect = pygame.Rect(self.brick_width * j, self.brick_height* i, self.brick_width, self.brick_height )
          temp_rect = Brick(self.brick_width * j, self.brick_height* i, self.brick_width, self.brick_height)          
          self.brick_list.append(temp_rect)

  def render(self, gameDisplay):
    for temp_rect in self.brick_list:
      gameDisplay.blit(self.img, temp_rect.get_render_rect())


if __name__ == "__main__":
  seed(1)
  g = Game()
  g.main()