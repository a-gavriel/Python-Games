import tkinter as tk
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))




def callback(event):
    root.focus_set()
    print ("clicked at", event.x, event.y)

root.bind("<Button-1>", callback)

root.bind('<Motion>', motion)
root.mainloop()