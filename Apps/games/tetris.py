import pygame
from random import randint

class Game:
  def __init__(self,rows,cols):
    self.crash = False
    self.score =  0    
    self.m = rows+2
    self.n = cols+2
    self.mat = [[0]* self.n for i in range(self.m)]    
    self.scale = 40
    self.game_height = self.m *self.scale
    self.game_width = self.n *self.scale
    self.gameDisplay = pygame.display.set_mode((self.game_width,self.game_height))    
    self.pos = 0,cols//2  
    self.i = 1
    self.j = self.n//2  
    self.pieces = {1:[[1],[1],[1],[1]],
                2:[[2,2,2],[0,0,2]],
                3:[[3,3,3],[3,0,0]],
                4:[[4,4,4],[0,4,0]],
                5:[[5,5],[5,5]]}
    self.colors = {1:(255,0,0),
                    2:(0,255,0),
                    3:(0,0,255),
                    4:(0,255,255),
                    5:(255,255,0),
                    7:(50,50,50)}
    self.fillborders()                
    self.new_piece()
  def fillborders(self):

    for j in range(self.n):
      self.mat[0][j] = 7
      self.mat[-1][j] = 7
    for i in range(self.m):
      self.mat[i][0] = 7
      self.mat[i][-1] = 7


  def transpose(self, piece):
    m = len(piece)
    n = len(piece[0])
    new_piece = [[0] * m for i in range (n)]
    for i,r in enumerate(piece):
      for j,e in enumerate(r):
        new_piece[j][i] = e
    return new_piece

  def flip_horizontal(self,piece):
    piece.reverse()
    return piece

  def rotate_clockwise(self, piece):
    flipped = self.flip_horizontal(piece)
    rotated = self.transpose(flipped)
    return rotated

  def random_rotate(self,piece):
    r = randint (0,3)
    result = piece
    if r > 2:
      result = self.rotate_clockwise(result)
    if r > 1:
      result = self.rotate_clockwise(result)
    if r > 0:
      result = self.rotate_clockwise(result)
    return result

  def new_piece(self):
    self.i = 1
    self.j = self.n//2  
    self.piece =  ( self.pieces[randint(1,5)] ) 


  def arrow_up(self):    
    self.piece = self.rotate_clockwise(self.piece)
    checking = 1
    while checking:
      checking = 0
      if self.j + len(self.piece[0]) >= self.n:
        self.j -= 1
        checking = 1
    

  def arrow_left(self):
    able = 1 
    for i,r in enumerate(self.piece):
      for j,e in enumerate(r):
        if e and self.mat[self.i + i][self.j + j-1]:
          able = able and 0
    if able:
      self.j -= 1

  def arrow_right(self):
    able = 1 
    for i,r in enumerate(self.piece):
      for j,e in enumerate(r):
        if e and self.mat[self.i + i][self.j + j+1]:
          able = able and 0
    if able:
      self.j += 1

  def arrow_down(self):
    self.i += 1

  def update(self):        
    new = self.check_col()
    self.check_rows()
    if new:
      self.new_piece()
  
  def check_col(self):    
    for i,r in enumerate(self.piece):
      for j,e in enumerate(r):
        if e and self.mat[self.i + i+1][self.j + j]:
          if self.i == 1:
            self.crash = True
            print("Lost :(")
            return 0
          self.place()
          return 1
          
  def check_rows(self):
    c = 0    
    i = self.m-2
    while(i > 0):
      if self.mat[i].count(0) != 0:
        i -= 1
      else:
        c += 1        
        new_row = [0]* self.n
        new_row[0] = 7
        new_row[-1] = 7  
        self.mat.pop(i)
        self.mat.insert(1,new_row)
    if c > 0:
      print(f'cleared {c} rows!')


  def place(self):
    for i,r in enumerate(self.piece):
      for j,e in enumerate(r):
        if e:
          self.mat[self.i + i][self.j + j] = e

  def render(self):
    self.gameDisplay.fill((0,0,0))
    for i,row in enumerate(self.mat):
      for j,e in enumerate(row):
        if e:
          rect = pygame.rect.Rect(( j * self.scale , i * self.scale,  self.scale,  self.scale)) 
          pygame.draw.rect(self.gameDisplay, self.colors[e] , rect )

    for i,row in enumerate(self.piece):
      for j,e in enumerate(row):
        if e:
          rect = pygame.rect.Rect( (self.j + j) * self.scale , (self.i + i) * self.scale,  self.scale,  self.scale)         
          pygame.draw.rect(self.gameDisplay, self.colors[e], rect )
    for i in range(self.m):
      pygame.draw.line(self.gameDisplay, (255,255,255), (0,self.scale * i), (self.scale * self.n,self.scale * i) )
    for j in range(self.n):
      pygame.draw.line(self.gameDisplay, (255,255,255), (self.scale * j, 0), (self.scale * j, self.scale * self.m) )
    pygame.display.flip()


def run():
  pygame.init()            
  clock = pygame.time.Clock()
  game = Game(20,10)
  while(not game.crash):    

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_LEFT]:
      game.arrow_left()
    if pressed[pygame.K_RIGHT]:
      game.arrow_right()
    if pressed[pygame.K_UP]:
      game.arrow_up()
    if pressed[pygame.K_DOWN]:
      game.arrow_down()

    game.update()
    game.render()
    
    events = pygame.event.get()      
    for event in events:
      if event.type == pygame.QUIT:
        game.crash = True
    clock.tick(10)
  pygame.quit()
  print("game finished!")
  

run()
