from PIL import Image, ImageTk
import tkinter as tk
import PIL
from tkinter import *
from PIL import Image, ImageDraw, ImageOps
import numpy as np
#import matplotlib.pyplot as plt

size = 300

def save():
  filename = 'number.png'
  # segundo parámetro es 2 para bilineal o 3 para bicubico
  #image2 = image1.resize((size, 28), 2)
  pil_img.save(filename)

def reset():
  global size
  cv.delete("all")
  draw.rectangle((0, 0, size, size), fill=(255))


root = tk.Tk()


array = np.random.randint(100,228, size=(size, size), dtype=np.uint8)

# --- PIL
#image0 = PIL.Image.new(mode='L', size=(size, size),color='white')  
pil_img = Image.fromarray(array)

img = ImageTk.PhotoImage(image=pil_img)

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=img)

btn_save = Button(text="Save", command=save)
btn_save.pack()

root.mainloop()
