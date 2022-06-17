import socket
import sys, pygame, random
from random import *


import socket



def joingame():
  # create a socket object
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

  local = 1

  # get local machine name
  host = "192.168.100.40" if local else input("ip: ")                

  port = 8000 if local else int(input("port: "))

  # connection to hostname on the port.
  server.connect((host, port))                               

  # Receive no more than 1024 bytes
  msgRaw = server.recv(1024)        
  msgDecoded =  (msgRaw.decode('ascii'))
  mydata = msgDecoded.split(",")
  player = int(mydata[0])

  while True:

    msg = input("X,Y:") 
    msg = str(player) + "," + msg   
    msgE = server.send(bytes(msg, 'ascii'))


    recvRaw = server.recv(1024)
    response = recvRaw.decode('ascii')
    print("Received:", response)

     

    if(msg == "-1"):
      break

  server.close()


joingame()