m1 = [[1,2,3],[4,5,6]]
m2 = [[1,4,5],[1,6,1],[0,2,3]]

################################################
#  While

def muestreM_w1(matriz):
  string = ""
  filas = len(matriz)
  cols = len(matriz[0])
  i = 0
  j = 0  
  while(i < filas):
    while(j < cols):
      elemento = matriz[i][j]
      string += str(elemento) + " "
      
      j += 1
    string += "\n"
    j = 0
    i += 1

  print(string)
  return(string)

##########
  
def muestreM_w2(matriz):  
  filas = len(matriz)
  cols = len(matriz[0])
  i = 0
  j = 0  
  while(i < filas):
    while(j < cols):
      elemento = matriz[i][j]
      print(elemento, end=" ")      
      j += 1
    print("")
    j = 0
    i += 1



################################################
#  For sin modificar matriz
def muestreM_f1(matriz):
  string = "" 
  for fila in matriz:
    for elemento in fila:
      string += str(elemento) + " " 
    string += "\n"
  print(string)
  return string



################################################
#  For por índices
def muestreM_f2(matriz):
  filas = len(matriz)
  cols = len(matriz[0])

  string = "" 
  for i in range(filas):
    for j in range(cols):
      elemento = matriz[i][j]
      string += str(elemento) + "\t"
    string += "\n"
    
  print(string)
  return string

def muestreM(matriz):
  return muestreM_f2(matriz)

####################################
def prod_escalarM(e,matriz):
  filas = len(matriz)
  cols = len(matriz[0])
  
  for i in range(filas):
    for j in range(cols):
      elemento = matriz[i][j] 
      matriz[i][j] = elemento * e
  
  return matriz

def diagonal(matriz):
  filas=len (matriz)
  cols=len(matriz[0])
  resultado = []
  for i in range(filas):
    for j in range(cols):
      if (i==j):
        elemento=matriz [i][j]
        resultado.append(elemento)
              
  return resultado 
















