from tkinter import *


def LAMBDA():
  ir_inicio(5)

def ventan2(v_main):
  global main, ventana
  v_main.withdraw()
  #main.withdraw()
  ventana = Toplevel()

  ventana.focus_force()

  Button(ventana,text="Boton 1!", height=6, width=30,
         command = ventana2_b1f).pack()

  Button(ventana,text="Boton 2!", height=6, width=30,
         command = lambda: ir_inicio(ventana) ).pack()
         #command = LAMBDA

  ventana.protocol("WM_DELETE_WINDOW",lambda:ir_inicio(ventana))

  
  

  ventana.mainloop()



def ventana2_b1f():
  global main, ventana
  ventana.destroy()
  main.deiconify()
  
def ir_inicio(desde):
  global main
  desde.destroy()
  main.deiconify()
  

def mainwindow():
  global main, data
  main = Tk()
  main.title("Ejemplo de Tkinter")
  main.minsize(750,450)
  main.resizable(width= False, height=False)


  c1 = Canvas(main,width=750,height=350, bg="#c8a2c8")
  c1.pack()

  #                 file="subcarpeta/nombre_imagen.extension"
  img = PhotoImage(file="formales.png")
  c1.create_image(352/2,352/2,image=img)



  b1 = Button(main,text="Press me!", width=30, command = lambda:ventan2(main))
  b1.place(x=0,y=100)

  b2 = Button(main,text="Boton 2!", height=6, width=30, command = boton2f)
  b2.pack()

  Titulo= Label(main, text="Welcome to Tkinter",
                bg="#20B2A9",fg = "#000000", font=380)
  Titulo.pack()

  data = StringVar()
  textField = Entry(main,textvariable=data).place(x=550,y=400)

  




  main.mainloop()


def boton2f():
  texto = data.get()
  T = 0
  if texto.lower() == "hola":
    print("Bienvenido")
    T = Label(main, text="Bienvenido",
              bg="#20B2A9",fg = "#000000", font=380)
    T.pack()
  else:
    print("You shall not pass!")
    T = Label(main, text="You shall not pass!",
              bg="#20B2A9",fg = "#000000", font=380)
    T.pack()
    
  
def f1():
  global x
  x = 0
  while not(x):
    x = 4
  print(x)

  
def f2():
  global x
  print(x)



mainwindow()
