#!/usr/bin/env python3

import socket


def cliente2():
    HOST = '127.0.0.1'  # The server's hostname or IP address

    PORT = 65432        # The port used by the server

    mensaje1 = 'mensaje1'
    mensaje2 = 'mensaje2'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(mensaje2, 'utf-8'))
        data = s.recv(1024)

    print('Received', repr(data))



cliente2()
