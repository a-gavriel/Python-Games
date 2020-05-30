import tkinter as tk
import datetime

filename = "stopwatch_timers.txt"

def readfile(mat = []):
	fp = open(filename, "a+") #opens as a+ instead of r to prevent error "file does not exist"	
	fp.seek(0)
	lines = fp.readlines()
	fp.close()
	if lines == []:
		print("No timers found!")
		name = input("New timer's name (leave blank for default): ")
		if name == "":
			name = "default"
		mat.append([name, 0])
		return mat
	else:		
		for line in lines:
			cleanline = (line.split("\n"))[0]
			if cleanline:			
				timer = cleanline.split(",")
				mat.append([timer[0],int(timer[1])])
		return mat



def update_clock( label):
  global root, counter, exit_
  counter += 1
  time = str(datetime.timedelta(seconds=counter))
  label.configure(text=time)
  if not exit_:
    root.after(1000, update_clock,  label)  
  else:
  	root.destroy()

def savefile(mat, tn):
	global root, counter, exit_	
	print("saving...")
	mat[tn][1] = counter
	f = open(filename, "w+")	# w+ truncates the file 	
	for row in mat:
		f.write(row[0] + "," + str(row[1]) + "\n")
	f.close()
	exit_ = True

def getinputs(mat):
	s = "\nWelcome!\nSelect a timer or write '-1' to create a new one:\n"
	for i in range(len(mat)):
		s += str(i) + "- "
		s += mat[i][0]
		s += "\n"
	return s + "Choose timer: "

def newcounter(mat):
	global counter
	name = input("New timer's name: ")
	counter = 0
	mat.append([name,0])
	savefile(mat, -1)

def App(mat, tn):
    global root, counter, exit_
    exit_ = False
    root = tk.Tk()
    labelName = tk.Label(text=" "+mat[tn][0]+" ", font=("Courier", 44))
    labelName.pack()
    label = tk.Label(text="", font=("Courier", 44))
    label.pack()

    update_clock(label)


    root.protocol("WM_DELETE_WINDOW",lambda: savefile( mat, tn))
    root.mainloop()

exit_ = False
i = "-1"
while (i == "-1"):
	mat = []
	readfile(mat)
	sinp = getinputs(mat)
	i = input(sinp)
	if i == "":
		break
	if i in "0123456789":
		tn = int(i)
		counter = mat[tn][1]	
		App(mat, tn)
	if i == "-1":
		newcounter(mat)


