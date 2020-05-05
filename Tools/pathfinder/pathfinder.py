import numpy as np    
from PIL import Image as PImage
from tkinter import *
from random import choice as Rchoice

img = PImage.open("testimg.png")
imgB = img.convert("1")
imgG = img.convert("L")
arr = (np.asarray(imgB))
arrG = np.asarray(imgG).copy()


savedImg = "img2.png"


#Image.fromarray(a)


scale = 20

def drawmatrix(canvas,matrix):
  for i in range(rows):
    for j in range(cols):
      val = matrix[i][j]
      color = "#" + str(hex(val)*3).replace('0x','')
      canvas.create_rectangle(j*scale,i*scale,(j+1)*scale,(i+1)*scale, fill=color)

(rows,cols) = arr.shape
print("Size is:",rows,"x",cols)

start = eval(input("write start position (i,j):"))
end = eval(input("write end position (i,j):"))

def invert(mat,max=255):
  for i in range(rows):
    for j in range(cols):
      mat[i][j] = 255 - mat[i][j]

arrGI = np.asarray(imgG).copy()   
invert(arrGI) 

def cmp(x, y):
  """
  Replacement for built-in function cmp that was removed in Python 3

  Compare the two objects x and y and return an integer according to
  the outcome. The return value is negative if x < y, zero if x == y
  and strictly positive if x > y.
  """

  return (x > y) - (x < y)


def string(matrix):
  for row in matrix:
    for e in row:
      s = str(e)
      print(s.zfill(3),end=" ")
    print("")


def alg(matrix, start, end, canvas):
  ci,cj = start[0],start[1] #current i,j
  ei,ej = end[0],end[1] #end i,j
  di,dj = (1,1)
  while (di or dj):

    di = cmp(ei,ci)
    dj = cmp(ej,cj)
    ti = ci+di
    tj = cj+dj

    if matrix[ti][cj] == False and matrix[ti][tj] == True:
      cj = tj
    elif matrix[ti][cj] == True and matrix[ti][tj] == False:
      ci = ti
    else:
      if Rchoice([0,1]):
        cj = tj
      else:
        ci = ti    
    canvas.create_rectangle(cj*scale,ci*scale,(cj+1)*scale,(ci+1)*scale, fill="cyan")    
    

def highest_skip(L,skip):
  h = 0
  i = 0
  options = []
  values = len(L)
  if skip == 0:
    h = 1
    i = 1
  if skip == -1:    
    while i < values:
      c = L[i] 
      if c > L[h]:
        options = [i]
        h = i
      elif c == L[h]:
        options.append(i)
      i += 1
  else:
    while i < values:
      c = L[i] 
      if i != skip and c > L[h]:
        options = [i]
        h = i
      elif c == L[h]:
        options.append(i)
      i += 1
  return Rchoice(options)


def alg2(matrix, start, end, canvas):
  ci,cj = start[0],start[1] #current i,j
  ei,ej = end[0],end[1] #end i,j
  
  prev = 4

  while not((ci==ei) and (cj==ej)):

    tl = matrix[ci,cj-1] #0
    tu = matrix[ci-1,cj] #1
    td = matrix[ci+1,cj] #2
    tr = matrix[ci,cj+1] #3

    possible = [tl,tu,td,tr]
    #print(possible,prev, 3-prev, end=" - ")
    new = highest_skip(possible,3-prev)
    dirs = ["←","↑", "↓", "→"]    
    print(dirs[new],end=" ")
    prev = new
    if new == 0:
      cj -= 1
    elif new == 1:
      ci -= 1
    elif new == 2:
      ci += 1
    else:
      cj += 1 
    #print(ci,cj, prev)  
    canvas.create_rectangle(cj*scale,ci*scale,
      (cj+1)*scale,(ci+1)*scale, fill="cyan")    
  print("Finish!")


def window(start,end, do):
  main = Tk()
  main.minsize(cols*scale,rows*scale)
  main.resizable(width= False, height=False)

  c = Canvas(main,width = cols*scale,height=rows*scale,bg="white")
  c.pack()
  drawmatrix(c,arrG)

  c.create_rectangle(start[1]*scale,start[0]*scale,
    (start[1]+1)*scale,(start[0]+1)*scale, fill="green")
  
  if do == 1:
    alg(arr, start, end, c)
  if do == 2:
    alg2(arrGI, start, end, c)

  c.create_rectangle(end[1]*scale,end[0]*scale,
    (end[1]+1)*scale,(end[0]+1)*scale, fill="red")


  #main.mainloop()

window(start,end, 0)
window(start,end, 1)
window(start,end, 2)