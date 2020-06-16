import pygame, random

class Game:
  def __init__(self,game_width,game_height):
    self.running = True
    self.score =  0
    self.gameDisplay = pygame.display.set_mode((game_width,game_height))
    self.imgs = []
    self.game_height = game_height
    self.game_width = game_width
    self.imgNames = ["blue.png","green.png","orange.png","purple.png","red.png","silver.png","yellow.png"]
    self.matrix = []
    self.clicked = [None,None]
    self.initmatrix()
    self.loadimgs()
  def initmatrix(self):
    for i in range(8):
      row = []
      for j in range(8):
        row.append(random.randint(0,6))
      self.matrix.append(row) 
  def print_matrix(self):
    print(" --------- ")
    for row in self.matrix:
      print(row)
    print(" --------- ")
  def loadimgs(self):
    for imgName in self.imgNames:
      self.imgs.append(pygame.image.load(imgName))
  def find_row(self,amount):
    for i in range(8):
      count = 0
      value = None
      for j in range(8):
        current = self.matrix[i][j]
        if value == current:
          count += 1
          if count == amount:
            return i,j-amount+1
        else:
          value = current
          count = 1
    return None,None
  def find_col(self,amount):  
    for j in range(8):  
      count = 0
      value = None
      for i in range(8):
        current = self.matrix[i][j]
        if value == current:
          count += 1
          if count == amount:
            return i-amount+1,j
        else:
          value = current
          count = 1
    return None,None
  def getvalue(self,i,j):
    if 0<=i<=7 and 0<=j<=7:
      return self.matrix[i][j]
    else:
      return random.randint(0,6)
  def break_tiles(self, i,j,Dir,amount):
    if Dir == 0:
      c = 0
      while(c < amount):
        for k in reversed(range(0,i+1)):
          self.matrix[k][j] = self.getvalue(k-1,j)        
        j += 1
        c += 1
    else:
      for k in reversed(range(0,i+amount)):        
        self.matrix[k][j] = self.getvalue(k-amount,j)



  def update(self):
    i,j = None,None    
    for amount in reversed(range(3,6)):
      i,j = self.find_row(amount)
      if i != None:
        return self.break_tiles(i,j,0,amount)
      else:
        i,j = self.find_col(amount)
        if i != None:
          return self.break_tiles(i,j,1,amount)
  def render_matrix(self):
    for i in range(8):
      pygame.draw.line(self.gameDisplay, (0,0,0), (0, 50*i), (400, 50*i))
      pygame.draw.line(self.gameDisplay, (0,0,0), (50*i,0 ), (50*i,400))
      for j in range(8):
        value = self.matrix[i][j]
        self.gameDisplay.blit(self.imgs[value], (j*50,i*50))
  def draw_clicked(self):
    for pos in self.clicked:
      if pos == None:
        pass
      else:
        i,j = pos
        x,y = j*50,i*50
        pygame.draw.line(self.gameDisplay, (255,0,0), (x, y), (x, y+50),5)
        pygame.draw.line(self.gameDisplay, (255,0,0), (x, y), (x+50, y),5)
        pygame.draw.line(self.gameDisplay, (255,0,0), (x+50, y), (x+50, y+50),5)
        pygame.draw.line(self.gameDisplay, (255,0,0), (x, y+50), (x+50, y+50),5)
  def render(self):
    self.gameDisplay.fill((0,255,255))
    self.render_matrix()
    self.draw_clicked()
    pygame.display.flip() #updates all screen
  def check_clic(self,position):
    #print("clicked on:", position)
    x,y = position
    j,i = int(x//50),int(y//50)
    if 0<=i<=7 and 0<=j<=7:
      if self.clicked[0] == None:
        self.clicked[0] = (i,j)
      elif self.clicked[0] != (i,j):        
        self.clicked[1] = (i,j)
        temp = self.matrix[i][j]
        i0,j0 = self.clicked[0]
        self.matrix[i][j] = self.matrix[i0][j0]
        self.matrix[i0][j0] = temp
        self.clicked = [None,None]
      else:
        self.clicked[0] = None  
    else:
      self.clicked[0] = None
    #print("saved clicks:",self.clicked)
    
def game():
  pygame.init()            
  clock = pygame.time.Clock()

  random.seed(1)
  game = Game(400,400)
  while(game.running):
    #agent stuff
    events = pygame.event.get()
    for event in events:
      # handle MOUSEBUTTONUP
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        game.check_clic(pos)
      if event.type == pygame.QUIT:
            game.running = False
    game.update()    
    game.render()

    clock.tick(10)

  print("game finished!")
  pygame.display.quit()
  pygame.quit()
game()









