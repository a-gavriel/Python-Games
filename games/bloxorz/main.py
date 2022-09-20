import pygame, sys
from numpy import random as np_rand
import numpy

class Game:

  def get_matrix(size) -> numpy.array:
    matrix = np_rand.randint(0,20,(size,size))
    for i in range(size):
      for j in range(size):
        if matrix[i][j]>1:
          matrix[i][j] = 1
    return matrix

  def __init__(self, scale = 40, matrix_size = 10):
    self.crash : bool = False       
    self.score : int =  0
    self.scale : int = scale
    self.matrix_size : int = matrix_size
    self.matrix : numpy.array = Game.get_matrix(matrix_size)
    self.game_width : int = matrix_size*scale
    self.game_height : int = self.game_width
    self.display_offset : int = 0
    self.gameDisplay = pygame.display.set_mode((self.game_width,self.game_height+self.display_offset))
    self.player : Player = Player(0,0)
    self.colors = {
      0: (255,255,255),
      1: (100,100,100)
    }

  def update(self):
    pass
    #self.ball.update(self, self.player)
    #self.wall.update(self.ball,self)    


  def shear2(a : numpy.array, strength=-1, shift_axis=0, increase_axis=1, edges='clip'):
    indices = numpy.indices(a.shape)
    indices[shift_axis] -= strength * indices[increase_axis]
    indices[shift_axis] %= a.shape[shift_axis]
    res = a[tuple(indices)]
    if edges == 'clip':
        res[indices[shift_axis] < 0] = 0
        res[indices[shift_axis] >= a.shape[shift_axis]] = 0
    return res

  def render(self):
    surface = pygame.Surface((self.game_width,self.game_height))
    surface_bg = pygame.Surface((self.game_width,self.game_height))
    surface_bg.fill((0,255,255))
    self.gameDisplay.fill((255,255,255))
    
    surface.fill((0,255,255))
    for i,row in enumerate(self.matrix):
      for j,tile in enumerate(row):
        rect = pygame.Rect(( j*self.scale , i*self.scale , self.scale, self.scale)) #Creo el rectangulo, x1, y1, w, h
        pygame.draw.rect(surface,self.colors[tile],rect ) #Dibujo el rectangulo
 
    for i in range(self.game_width // self.scale):
      pygame.draw.line(surface, (255,255,255), (i*self.scale, 0), (i*self.scale, self.game_height))
      pygame.draw.line(surface, (255,255,255), (0, i*self.scale), (self.game_width, i*self.scale))

    self.player.render(surface, self.scale)
    surface_game = pygame.transform.rotozoom(surface, 0, 0.5)

    surface_bg.blit(surface_game, (0,self.game_height//2) )

    surface_array : numpy.array = pygame.surfarray.array2d(surface_bg)
    new_surfarray = Game.shear2(surface_array)
    new_surface = pygame.surfarray.make_surface(new_surfarray)

    self.gameDisplay.blit(new_surface, (0,-self.game_height//4))
    pygame.display.flip()


class Player:

  STANDING = 0
  VERTICAL = 1
  HORIZONTAL = 2

  POSITIONS = {
    0 : "STANDING",
    1 : "VERTICAL",
    2 : "HORIZONTAL"
  }

  MOVEMENT_KEYS = {
      pygame.K_LEFT: (0,-1),
      pygame.K_RIGHT: (0,1),
      pygame.K_UP: (-1,0),
      pygame.K_DOWN: (1,0)
    }

  def __init__(self, i, j):
    self.i = i
    self.j = j
    self.rotation = Player.STANDING
    

  def check_valid_position(self, matrix, new_i, new_j, new_rotation) -> bool:
    m , n = len(matrix), len(matrix[0])

    y1 = y2 = new_i
    x1 = x2 = new_j

    if new_rotation == Player.HORIZONTAL:
      x2 = x1 + 1
    if new_rotation == Player.VERTICAL:
      y2 = y1 + 1
  
    if x1 < 0 or x2 >= m:
      return False
    if y1 < 0 or y2 >= n:
      return False
    if matrix[y1][x1] == 0 and matrix[y2][x2] == 0:
      return False

    return True

  def update(self, direction, matrix):


    new_i,new_j = self.i, self.j
    new_rotation = self.rotation
    new_movement = Player.MOVEMENT_KEYS[direction]


    if new_rotation == Player.STANDING:
      if direction == pygame.K_UP or direction == pygame.K_DOWN:
        new_rotation = Player.VERTICAL

      elif direction == pygame.K_LEFT or direction == pygame.K_RIGHT:
        new_rotation = Player.HORIZONTAL

      new_i,new_j = new_i + new_movement[0], new_j + new_movement[1]
      if direction == pygame.K_UP or direction == pygame.K_LEFT:
        new_i,new_j = new_i + new_movement[0], new_j + new_movement[1]
    
    elif new_rotation == Player.HORIZONTAL:
      if direction == pygame.K_LEFT or direction == pygame.K_RIGHT:
        new_rotation = Player.STANDING

      new_i,new_j = new_i + new_movement[0], new_j + new_movement[1]
      if direction == pygame.K_RIGHT:
        new_i,new_j = new_i + new_movement[0], new_j + new_movement[1]
    

    elif new_rotation == Player.VERTICAL:
      if direction == pygame.K_UP or direction == pygame.K_DOWN:
        new_rotation = Player.STANDING

      new_i,new_j = new_i + new_movement[0], new_j + new_movement[1]
      if direction == pygame.K_DOWN:
        new_i,new_j = new_i + new_movement[0], new_j + new_movement[1]

    
    print(f'Rotation:{Player.POSITIONS[self.rotation]} -> {Player.POSITIONS[new_rotation]}')
    
    if self.check_valid_position(matrix, new_i, new_j, new_rotation):
      self.i, self.j = new_i, new_j
      self.rotation = new_rotation


  def render(self, gameDisplay, scale : int):
    offset = scale//10

    width = scale-2*offset
    height = scale-2*offset

    if self.rotation == Player.HORIZONTAL:
      width = (2*scale)-2*offset
    elif self.rotation == Player.VERTICAL:
      height = (2*scale)-2*offset
    
    rect = pygame.Rect(( offset + self.j*scale , offset + self.i*scale , width, height)) 

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
            if event.key in Player.MOVEMENT_KEYS:
                game.player.update(event.key, game.matrix)
            if event.key == pygame.K_SPACE:
                alive= False

    game.render()
    
    clock.tick(60)#Define los FPS

    
  #End while
  pygame.quit()




if __name__ == "__main__":
  main()
