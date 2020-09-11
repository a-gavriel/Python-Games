#!/usr/bin/python3           # This is server.py file
import socket                                         
from threading import Thread


clients = []
trds = []
clients_data = ["0,10,10","1,100,100"]
client_number = -1
total_clients = 2


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
hostname = socket.gethostname()

# get local machine name
host = socket.gethostbyname(hostname)
port = 8000
try:
  port = int(input("port: "))
except:
  print(f"using port {port}")
# bind to the port
serversocket.bind((hostname, port))

# queue up to total_clients requests
serversocket.listen(total_clients)                                           


def close_all():
  for clientsocket, addr in clients:
    print("closing address: ", addr)
    try:
      clientsocket.close()
    except:
      pass

def clientHandler(clientsocket, addr, client_number):
  global clients_data
  print("New Client!")

  msg = clients_data[client_number]
  clientsocket.sendto(msg.encode('ascii'), addr)
  #c.sendto(data, client)
  dataDecoded = ""
  while True:
    dataRaw = clientsocket.recv(1024)
    dataDecoded = dataRaw.decode('ascii')
    print(dataDecoded)

    # msg = "Server received: " + dataDecoded +" from you:"+ str(addr)
    # clientsocket.sendto(msg.encode('ascii'), addr)

    if dataDecoded == "-1": 
      print("Closing current connection")   
      clientsocket.close()
      clients.pop(clients.index((clientsocket, addr)))
      break
    elif dataDecoded == "-2":
      print("Closing all connections")
      close_all()
      clients.clear()
      break
    else:
      received_vals = dataDecoded.split(",")
      player = int(dataDecoded[0])
      clients_data[player] = received_vals
      msg = clients_data[0] + ":" + clients_data[1]
      clientsocket.sendall(msg.encode('ascii'))


while True:
  # establish a connection
  clientsocket,addr = serversocket.accept()
  print("Got a connection from %s" % str(addr))
  client_number += 1
  clients.append((clientsocket, addr))
  t = Thread(target=clientHandler, args = (clientsocket, addr, client_number))
  trds.append(t)
  t.start()
