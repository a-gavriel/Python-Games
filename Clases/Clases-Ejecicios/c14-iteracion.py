"""
Escriba una función moda(num) que reciba un número y retorne el dígito
  que se repite más veces, si no hay dígitos que se
  repiten retorna:  -1

>>> moda(114443)
4

>>> moda(1475)
-1

Extra: Retorne todos dígitos que se repiten más veces

>>> moda(55513222)
[5,2]

>>> moda(7896)
[-1]

"""

############################################
"""
Retorna las posiciones de los digitos mayores de la lista

"""
def mayor_i(lista,mayor, mayor_pos, i):
  if i == len(lista):
    return (mayor, mayor_pos)
  else:
    actual = lista[i]
    if actual > mayor:
      mayor = actual
      mayor_pos = [i]
    elif actual == mayor:
      mayor_pos.append(i)
    return mayor_i(lista,mayor, mayor_pos, i+1)

"""
Contabiliza cuantos dígitos hay en el número
  si el dígito no está, lo agrega a la lista de digitos 
  si el dígito está, agrega 1 en las repeticiones del dígito  
  
"""
def agregar(digitos, repeticiones, digito, i):
  if i == len(digitos):
    digitos.append(digito)
    repeticiones.append(1)
    return True
  elif digito == digitos[i]:
    repeticiones[i] = repeticiones[i] + 1
    return True
  else:
    return agregar(digitos, repeticiones, digito, i+1)
    

"""
Cuenta las repeticiones de los dígitos de un número,
  y retorna una lista con los dígitos que más se repiten.
  Si ningún dígito se repite, retorna [-1]
  
"""
def moda_aux(num, digs, reps):
  if num == 0:
    mayor, mayor_pos = mayor_i(reps, reps[0],[] ,0)
    if mayor == 1:
      return [-1]    
    digitosRep = digs_por_i(digs, mayor_pos,[],0)
    return digitosRep
  else:
    ultimo = num % 10
    agregar(digs, reps, ultimo, 0)
    return moda_aux(num//10, digs, reps)
    
"""
Recibe una lista digs, y una lista de posciones indices y retorna
    una lista compendida por los datos en las posciones indicadas por
    la lista indices
"""
def digs_por_i(digs, indices,resultado, i):
  if (len(digs) == i) or (indices == []):
    return resultado
  else:    
    if i == indices[0]:
      actual = digs[i]
      resultado.append(actual)
      indices = indices[1:]
    return digs_por_i(digs, indices,resultado, i+1 )



def moda(num):
  if num == 0:
    return [-1]
  return moda_aux(num, [],[])






############################################

# 6a.9 

def mayor_xfila_aux (matriz,filas,cols,i,j, resultado):
    if filas == i:
        return resultado
    elif cols == j:
        return mayor_xfila_aux (matriz,filas,cols, i+1,0,resultado)
    else:
        actual =  matriz[i][j]
        if (actual > resultado):
          resultado = actual
        return mayor_xfila_aux (matriz,filas,cols, i,j+1, resultado)
    
    
def mayor_xfila(matriz):
  filas = len(matriz)
  cols = len(matriz[0])
  return mayor_xfila_aux (matriz,filas,cols,0,0, matriz[0][0])


      ############################################

def mayor_xcol_aux (matriz, filas, cols,i,j, resultado):
    if cols == j: #  cols = len(matriz[0])
        return resultado
    elif filas == i: # filas = len(matriz)
        return mayor_xcol_aux (matriz,filas,cols,0,j+1,resultado)
    else:
        actual =  matriz[i][j]
        print(actual)
        if (actual > resultado):
          resultado = actual
        return mayor_xcol_aux (matriz,filas,cols, i+1,j, resultado)
    


def mayor_xcol(matriz):
  filas = len(matriz)
  cols = len(matriz[0]) # cantidad de elementos en una fila
  return mayor_xcol_aux(matriz, filas, cols, 0,0, matriz[0][0])




    
