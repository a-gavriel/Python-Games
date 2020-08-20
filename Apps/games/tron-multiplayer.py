import socket
import sys, pygame, random
from random import *


import socket

def joingame():
  # create a socket object
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

  # get local machine name
  host = "192.168.100.40"                       

  port = 4000

  # connection to hostname on the port.
  s.connect((host, port))                               

  # Receive no more than 1024 bytes
  msg = s.recv(1024)        
  print (msg.decode('ascii'))


  while True:
    msg = input("New message: ")
    msgE = s.send(bytes(msg, 'ascii'))

    resp = s.recv(1024)
    respD = resp.decode('ascii')

    print("response: "+respD)

    if(msg == "-1"):
      break

  s.close()




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
    self.players = [Player(self.scale, 1, 1, 1), Player(self.scale, 10, 10, 2)]
    self.dic = {0:(255,255,255),
                1:(255,0,0),
                2:(0,255,0)}

  def update(self):

    for player in self.players:
      self.crash = self.crash or player.update(*self.size, self.mat)

    #self.ball.update(self, self.player)
  def render(self):
    self.gameDisplay.fill((0,255,255))

    for i,row in enumerate(self.mat):
      for j,e in enumerate(row):
        rect = pygame.rect.Rect(( j * self.scale , i * self.scale,  self.scale,  self.scale))         
        pygame.draw.rect(self.gameDisplay, self.dic[ e ] , rect )

    for player in self.players:
      player.render(self)
    pygame.display.flip()
    

def hostgame():
  pass


## importing socket module
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")











def run():
  pygame.init()            
  clock = pygame.time.Clock()
  
  game = Game(400,400)
  #initializegame
  #render game

  

  while(not game.crash):    

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_LEFT]:
      game.players[0].dir_ = 1
    if pressed[pygame.K_RIGHT]:
      game.players[0].dir_ = 2
    if pressed[pygame.K_UP]:
      game.players[0].dir_ = 3
    if pressed[pygame.K_DOWN]:
      game.players[0].dir_ = 4

    if pressed[pygame.K_a]:
      game.players[1].dir_ = 1
    if pressed[pygame.K_d]:
      game.players[1].dir_ = 2
    if pressed[pygame.K_w]:
      game.players[1].dir_ = 3
    if pressed[pygame.K_s]:
      game.players[1].dir_ = 4
    
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
