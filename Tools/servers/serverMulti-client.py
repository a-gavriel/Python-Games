#!/usr/bin/python3           # This is server.py file
import socket                                         
from threading import Thread

clients = []

trds = []


# create a socket object
serversocket = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
hostname = socket.gethostname()

# get local machine name
host = socket.gethostbyname(hostname)
port = 8000
try:
	port = int(input("port: "))
except:
	print("using port 4000")
# bind to the port
serversocket.bind((hostname, port))

# queue up to 5 requests
serversocket.listen(5)                                           


def close_all():
	for clientsocket, addr in clients:
		print("closing address: ", addr)
		try:
			clientsocket.close()
		except:
			pass

def clientHandler(clientsocket, addr):
	print("New Client!")

	msg = 'Thank you for connecting'+ "\r\n"
	clientsocket.sendto(msg.encode('ascii'), addr)
	#c.sendto(data, client)
	dataD = ""
	while True:
		data = clientsocket.recv(1024)
		dataD = data.decode('ascii')
		print(dataD)

		msg = "Server received: " + dataD +" from you:"+ str(addr)
		clientsocket.sendto(msg.encode('ascii'), addr)

		if dataD == "-1":	
			print("Closing current connection")   
			clientsocket.close()
			clients.pop(clients.index((clientsocket, addr)))
			break
		if dataD == "-2":
			print("Closing all connections")
			close_all()
			break




while True:
	# establish a connection
	clientsocket,addr = serversocket.accept()      

	print("Got a connection from %s" % str(addr))
	clients.append((clientsocket, addr))
	t = Thread(target=clientHandler, args = (clientsocket, addr))
	trds.append(t)
	t.start()
