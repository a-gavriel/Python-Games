import random
import socket
import pickle
import threading
import time
import pandas as pd
from tkinter import *
from os import path
from random import randint
score1 = 0

window = Tk()
window.title("Cliente")
window.geometry('350x200')
lbl = Label(window, text="Nombre: ")
lbl.grid(column=0, row=0)
name = Entry(window,width=10)
name.grid(column=1, row=0)
nam = "Noel"

listbox = Listbox(window, height=3)
listbox.grid(column=1, row=1)
firstime = True

multicast_addr = '224.0.0.3'
bind_addr = '0.0.0.0'          
port = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((bind_addr, port))

if(firstime):
    values=["Load", "scores"] 
    data=pickle.dumps(values)
    sock.sendto(data, (multicast_addr, port))
    firstime = False

def thread_function():
    while not firstime:
        message, address = sock.recvfrom(255)
        values = pickle.loads(message)
        if(values[0] == "scores"):
            listbox.insert(END, values[1])
        elif values[0] != nam:
            print(values)
        
x = threading.Thread(target=thread_function)
x.start()
def add():
    values=[name.get(), btn.cget('text'),0,0,0] 
    print("ADDsending:",values)
    data=pickle.dumps(values)
    sock.sendto(data, (multicast_addr, port))

def update():
    values=[name.get(), "Update", 84,1,2]
    print("UPDATEsending",values)
    data=pickle.dumps(values)
    sock.sendto(data, (multicast_addr, port))

btn = Button(window, text="Add", command=add)
btn.grid(column=2, row=0)

btn2 = Button(window, text="Update", command=update)
btn2.grid(column=3, row=0)



window.mainloop()
