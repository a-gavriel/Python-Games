import tkinter as tk
import datetime


def update_clock( label, label2 ):
	global root, counter, exit_, continue_flag, last_timestamp
	if continue_flag:
		counter += 1
	total_time = str(datetime.timedelta(seconds=counter))
	current_time = str(datetime.timedelta(seconds=counter - last_timestamp))
	label.configure(text= "Total " + total_time)
	label2.configure(text=current_time)
	if not exit_:
		root.after(1000, update_clock,  label, label2)  
	else:
		root.destroy()

def pause(e):
	global continue_flag
	continue_flag = not (continue_flag)

def new_stop(e):
	global counter, last_timestamp
	last_timestamp = counter
	#newlabel = tk.Label(text="", font=("Courier", 44))
	#new_label.pack()

def exit_app():
	global exit_
	exit_ = True

def app():
	global root, counter, exit_, continue_flag, last_timestamp
	last_timestamp = 0
	continue_flag = True
	counter = 0
	exit_ = False
	root = tk.Tk()	
	label = tk.Label(text="", font=("Courier", 44))
	label.pack()
	label2 = tk.Label(text="", font=("Courier", 34))
	label2.pack()

	update_clock(label, label2)

	root.bind('<p>', pause)
	root.bind('<space>', new_stop)
	root.protocol("WM_DELETE_WINDOW", exit_app)
	root.mainloop()

app()