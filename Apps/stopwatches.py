"""
Original code: 

https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter

# for python 3.x use 'tkinter' rather than 'Tkinter'
import Tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()




"""
import tkinter as tk
import datetime


def update_clock( label):
  global root, counter
  counter += 1
  time = str(datetime.timedelta(seconds=counter))
  label.configure(text=time)
  root.after(1000, update_clock,  label)  

def save(tn):
	global root, counter
	print("saving")
	f = open("timers.txt", "r")
	lines = f.readlines()
	f.close()
	print(lines)
	if lines != []:
		lines[tn-1] = str(counter) + "\n"
	else:
		lines = [str(counter) + "\n"]
	print(lines)
	
	f = open("timers.txt", "w")
	f.truncate(0)
	for l in lines:
		f.write(l)
	f.close()
	root.destroy()

def App(tn):
    global root, counter
    root = tk.Tk()
    label = tk.Label(text="", font=("Courier", 44))
    label.pack()

    update_clock(label)


    root.protocol("WM_DELETE_WINDOW",lambda: save( tn))
    root.mainloop()


i = "0"
while (i == "0"):
	f = open("timers.txt", "r")
	lines = f.readlines()
	f.close()
	i = input("Timers:\n0-Exit\n1-Design\nChoose timer:")
	if i in "123":
		tn = int(i)
		t_chosen = ((lines[tn-1]).split("\n"))[0] if (lines != []) else ""
		print(lines,tn,  t_chosen)
		counter = int(t_chosen) if (t_chosen != "" ) else 0		
		App(tn)


