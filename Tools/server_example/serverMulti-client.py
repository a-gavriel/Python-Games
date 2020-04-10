#!/usr/bin/python3           # This is server.py file
import socket                                         
from threading import Thread

clients = []

trds = []


# create a socket object
serversocket = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           


def clientHandler(clientsocket, addr):
	print("New Client!")

	msg = 'Thank you for connecting'+ "\r\n"
	clientsocket.sendto(msg.encode('ascii'), addr)
	#c.sendto(data, client)
	while True:
		data = clientsocket.recv(1024)
		dataD = data.decode('ascii')
		print(dataD)

		msg = "Server received: " + dataD +" from you:"+ str(addr)
		clientsocket.sendto(msg.encode('ascii'), addr)

		if dataD == "-1":	
			print("Closing current connection")   		
			break
	clientsocket.close()


while True:
	# establish a connection
	clientsocket,addr = serversocket.accept()      

	print("Got a connection from %s" % str(addr))
	clients.append(addr)
	t = Thread(target=clientHandler, args = (clientsocket, addr))
	trds.append(t)
	t.start()

	
	

	