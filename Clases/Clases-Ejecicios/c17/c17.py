

m1= [[0,100,3], [100,9,10]]
m2 = [[0,0,0], [0,0,0], [1,3,5]]

"""
Documentación para entradas y salidas
https://docs.python.org/3/tutorial/inputoutput.html

"""


def mostrarM(matriz):
  string = ""
  for fila in matriz:
    for ele in fila:
     string += str(ele) + "\t"
    string += "\n"
  return string


  
def escribir(matriz):
  with open ("file.txt","r+") as f:
    string = mostrarM(matriz)
    f.truncate(0)
    f.write(string)



def leer():
  f = open("file.txt","r")
  filas = f.readlines()
  matriz = []
  for fila in filas:
    elementos = fila.split("\t")[:-1]
    fila_nueva = []
    for ele in elementos:
      numero = int(ele)
      fila_nueva.append(numero)
      
    matriz.append(fila_nueva)
        
  f.close()
  return matriz



nombre = input("Nombre: ")
if nombre == "Alexis":
  print("Hola!!",nombre)
else:
  print("Adios!!")





'''

CSV
https://docs.python.org/3/library/csv.html

Para abrir un archivo CSV (comma separated values)
import csv
f = open("temp1 - Sheet1.csv")
excel = csv.reader(f)
for row in excel:
  print(row)


'''






  
