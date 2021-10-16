import pygame, sys
from numpy import random as np_rand

class Game:

  def get_matrix(size):
    matrix = np_rand.randint(0,20,(size,size))
    for i in range(size):
      for j in range(size):
        if matrix[i][j]>1:
          matrix[i][j] = 1
    return matrix

  def __init__(self,scale=20, matrix_size = 20):
    self.crash = False       
    self.score =  0
    self.scale = scale
    self.matrix_size = matrix_size
    self.matrix = Game.get_matrix(matrix_size)
    self.game_width = matrix_size*scale
    self.game_height = self.game_width
    self.display_offset = 0
    self.gameDisplay = pygame.display.set_mode((self.game_width,self.game_height+self.display_offset))
    self.player = Player(0,0)
    self.colors = {
      0: (255,255,255),
      1: (100,100,100)
    }

  def update(self):
    pass
    #self.ball.update(self, self.player)
    #self.wall.update(self.ball,self)    
  def render(self):
    self.gameDisplay.fill((0,255,255))
    
    for i,row in enumerate(self.matrix):
      for j,tile in enumerate(row):
        rect = pygame.Rect(( j*self.scale , i*self.scale , self.scale, self.scale)) #Creo el rectangulo, x1, y1, w, h
        pygame.draw.rect(self.gameDisplay,self.colors[tile],rect ) #Dibujo el rectangulo

    self.player.render(self.gameDisplay, self.scale)
    pygame.display.flip()


class Player:
  def __init__(self, i, j):
    self.i = i
    self.j = j
    self.rotation = 0
  def update(self, direction, matrix):

    new_i,new_j = self.i , self.j
    

    d = {
      pygame.K_LEFT: (0,-1),
      pygame.K_RIGHT: (0,1),
      pygame.K_UP: (-1,0),
      pygame.K_DOWN: (1,0)
    }

    new_i,new_j = new_i + d[direction][0], new_j + d[direction][1]

    m , n = len(matrix), len(matrix[0])
    if new_i < 0:
      new_i = 0
    if new_i >= m:
      new_i = m-1
    if new_j < 0:
      new_j = 0
    if new_j >= n:
      new_j = n - 1

    if (new_i != self.i) or (new_j != self.j):
      if matrix[new_i][new_j] > 0:
        self.i, self.j = new_i, new_j


  def render(self, gameDisplay, scale):
    offset = scale//10
    #rect = pygame.Rect(( self.j*scale , self.i*scale , scale, scale)) #Creo el rectangulo, x1, y1, w, h
    rect = pygame.Rect(( offset + self.j*scale , offset + self.i*scale , scale-2*offset, scale-2*offset)) #Creo el rectangulo, x1, y1, w, h

    pygame.draw.rect(gameDisplay,(150,150,0),rect ) #Dibujo el rectangulo

def main():
  pygame.init()          #inicializo pygame  
  clock = pygame.time.Clock() #inicializo el reloj para los FPS
  alive = True
  game = Game()
  
  while alive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #se cierra desde la equis
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                game.player.update(event.key, game.matrix)
            if event.key == pygame.K_SPACE:
                alive= False

    game.render()
    
    clock.tick(60)#Define los FPS

    
  #End while
  pygame.quit()




if __name__ == "__main__":
  pass
  #main()
