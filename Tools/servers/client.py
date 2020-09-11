#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
hostname = socket.gethostname()

# get local machine name
host = socket.gethostbyname(hostname)
port = 8000
try:
	port = int(input("port: "))
except:
	print(f"using port {port}")

# connection to hostname on the port.
s.connect((hostname, port))

# Receive no more than 1024 bytes
msg = s.recv(1024)        
print (msg.decode('ascii'))


while True:
	msg = input("New message: ")
	msgE = s.send(bytes(msg, 'ascii'))

	resp = s.recv(1024)
	respD = resp.decode('ascii')

	print("response: "+respD)

	if(msg == "-1" or msg == "-2"):
		break

s.close()
