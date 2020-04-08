import random
import socket
import pickle
import threading
import time
import pandas as pd
from tkinter import *
from os import path
from random import randint


window = Tk()
window.title("Server")
window.geometry('350x200')
multicast_addr = '224.0.0.3'
bind_addr = '0.0.0.0'          
port = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((bind_addr, port))
name = "Server"
def thread_function():
    while True:
        message, address = sock.recvfrom(255)
        values = pickle.loads(message)
        if(values[0] != name and values[1] == "scores"):
            df = pd.read_csv('data.csv', delimiter = ',')
            for index, row in df.iterrows():
                print(row[1])
                values=["scores", row[0], row[1],row[2],row[3]]
                data=pickle.dumps(values)
                sock.sendto(data, (multicast_addr, port))
        elif(values[0] != name and values[1] == "Add"):
            print("addRECEIVED: ", values)
            df = pd.read_csv('data.csv', delimiter = ',')
            df = df.append({'name': values[0], "score":values[1], "x":values[2], "y":values[3]}, ignore_index=True)
            df.to_csv('data.csv', index=False)
        elif (values[0] != name and values[1] == "Update"):
            print("updateRECEIVED: ", values)
            df = pd.read_csv('data.csv', delimiter = ',')
            df.loc[df['name'] == values[0], 'score'] = float(values[2])
            df.loc[df['name'] == values[0], 'x'] = float(values[3])
            df.loc[df['name'] == values[0], 'y'] = float(values[4])
            df.to_csv('data.csv', index=False)

x = threading.Thread(target=thread_function)
x.start()

window.mainloop()

