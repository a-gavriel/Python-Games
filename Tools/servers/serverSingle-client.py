#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
hostname = socket.gethostname()

# get local machine name
host = socket.gethostbyname(hostname)
port = 4000
try:
	port = int(input("port: "))
except:
	print("using port 4000")

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
	# establish a connection
	clientsocket,addr = serversocket.accept()      

	print("Got a connection from %s" % str(addr))
	
	msg = 'Thank you for connecting'+ "\r\n"
	clientsocket.send(msg.encode('ascii'))

	while True:
		data = clientsocket.recv(1024)
		dataD = data.decode('ascii')
		print(dataD)

		msg = "Server received: " + dataD +" from you:"+ str(addr)
		clientsocket.send(msg.encode('ascii'))
		if(dataD == "-1"):
			print("Closing current connection")    
			break
	clientsocket.close()

	print("Waiting for new connection")
