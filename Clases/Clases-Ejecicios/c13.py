
def muestreM_string(matriz,i,j,string):
  if i == len(matriz):#tras recorrer todas las filas
    print(string)
    return string
  elif j == len(matriz[i]):#tras recorrer una fila
    string = string + "\n"
    return muestreM_string(matriz,i+1,0, string)
  else:#para cada elemento
    elemento = matriz[i][j]
    string = string + str(elemento) + "\t"
    return muestreM_string(matriz,i,j+1, string)

def muestreM_s(matriz):
  return muestreM_string(matriz,0,0,"")

#######################################

def muestreM_print(matriz,i,j):
  if i == len(matriz):#tras recorrer todas las filas
    return matriz
  elif j == len(matriz[i]):#tras recorrer una fila
    print("",end="\n")
    return muestreM_print(matriz,i+1,0)
  else:#para cada elemento
    elemento = matriz[i][j]
    print(elemento,end="\t")
    return muestreM_print(matriz,i,j+1)

def muestreM_p(matriz):
  return muestreM_print(matriz,0,0)




#######################################
def prod_escalarM_aux(e,matriz,i,j):
  if len(matriz) == i:
    return matriz
  elif len(matriz[i]) == j:
    return prod_escalarM_aux(e,matriz,i+1,0)
  else:
    elem = matriz[i][j]
    prod = elem * e
    matriz[i][j] = prod
    return prod_escalarM_aux(e,matriz,i,j+1)



def prod_escalarM(e,matriz):
  return prod_escalarM_aux(e,matriz,0,0)



############################################



m1 = [[1,1],[2,3],[10,11]]
m2 = [[1,1,1],[2,3,4],[10,11,12]]

def diagonal_aux(matriz, i, j, resultado):
  if len(matriz)==i:
    return resultado
  elif len(matriz[i])==j:
    return diagonal_aux(matriz,i+1,0, resultado)
  elif i==j:
    elem = matriz[i][j]
    resultado.append(elem)
  return diagonal_aux(matriz,i,j+1, resultado)


def diagonal2(matriz,i,resultado):
	if i == len(matriz):
		return resultado
	else:
		elem = matriz[i][i]
		resultado.append(elem)
		return diagonal_aux(matriz,i, resultado)


def diagonal(matriz):
  return diagonal_aux(matriz,0,0,[])


############################################

# 6a.8

def sumaM_aux(matriz, i, j, resultado):
  if len(matriz)==i:
    return resultado
  elif len(matriz[i])==j:
    return sumaM_aux(matriz,i+1,0, resultado)
  else:
    elem = matriz[i][j]
    resultado = resultado + elem
    return sumaM_aux(matriz,i,j+1, resultado)
     
def sumaM(matriz):
  return sumaM_aux(matriz,0,0,0)



def promedio(matriz):
  suma = sumaM(matriz)
  
  filas = len(matriz)
  cols = len(matriz[0])
  elem_tot = filas * cols
  promedio = suma / elem_tot
  return promedio








  


