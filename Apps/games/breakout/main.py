
import sys, pygame, random
from random import *
from game_objects import *
from constants import *
from physics import *




class Game:
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.gameDisplay = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.mouse.set_visible(0)       # turn off mouse pointer
    self.crash = False
    self.player = Player()
    self.ball = Ball()
    self.score =  0
    self.game_paused = False


    self.brick_img = pygame.image.load("brick-1.png").convert()
    self.brick_list = []
    self.create_bricks()

  def update(self):
    #self.ball.update(self, self.player)
    #self.wall.update(self.ball,self)   
    if Collide(self.ball.Rect, self.player.Rect):
      ball_player_collision(self.ball, self.player)
    

    collided_brick_i = self.ball.Rect.collidelist(self.brick_list)
    if collided_brick_i != -1:
      ball_brick_collision(self.ball, self.brick_list[collided_brick_i])
      self.brick_list.pop(collided_brick_i)
    
    if self.ball.update():
      self.ball.spawn()

  def create_bricks(self):
    brick_width = 32
    brick_height = 13
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
          temp_rect = pygame.Rect(brick_width * j, brick_height* i, brick_width, brick_height )
          self.brick_list.append(temp_rect)

  def main(self):
    
    
    while(not self.crash):
      self.clock.tick(GAME_FPS)

      # process key presses
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              self.game_paused = not self.game_paused

      
      if not self.game_paused:
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:                        
            self.player.move(-5,0)  
        if keys[pygame.K_RIGHT]:                  
            self.player.move(5,0)
        if keys[pygame.K_SPACE]:
            self.ball.start_ball()

        self.update()
      
      self.render(self.game_paused)

  def render(self, game_paused):
    bg_color = ( 0x2F, 0x4F, 0x4F )
    self.gameDisplay.fill(bg_color) #clean display
    self.player.render(self.gameDisplay)
    self.ball.render(self.gameDisplay)

    for current_brick_rect in self.brick_list:
      self.gameDisplay.blit(self.brick_img, current_brick_rect)

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
    



if __name__ == "__main__":
  seed(1)
  g = Game()
  g.main()