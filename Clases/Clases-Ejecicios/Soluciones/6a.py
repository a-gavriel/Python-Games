##########################################
#1
def vectorAux (vector, indice, resultado):
    tamaño= len(vector)
    numerito = (-1*tamaño)-1
    if numerito == indice:
        return resultado
    else:
        dato=vector[indice]
        resultado.append(dato)
        return vectorAux(vector,indice-1,resultado)
    

def vector_invert (vector):
    return vectorAux(vector,-1,[])
    
##########################################
#2
def prodEAux(escalar,vector, indice, tamaño): 
    #tamaño= len(vector)
    if indice == tamaño:
        return vector
    else:
        valor = vector[indice] * escalar
        vector[indice] = valor
        return prodEAux(escalar,vector,indice+1, tamaño)
        

def prod_escalar(escalar,vector):
    return prodEAux(escalar,vector,0,len(vector))

##########################################
#3    
def prodAux (v,w,indice,resultado,tamaño):
    if indice == tamaño:
        return resultado
    else:
        valor=v[indice]* w[indice]
        resultado += valor
        return prodAux (v,w,indice+1,resultado,tamaño)

def prod_vector(v,w):
    return prodAux(v,w,0,0, len(v))




##########################################
#4
def comparar (vec1, vec2, posicion):
    if len(vec1)!=len(vec2):
        return False
    elif len(vec1)==posicion:
        return True
    else: 
        d1=vec1[posicion]
        d2=vec2[posicion]
        if d1==d2:
            return comparar(vec1,vec2,posicion+1)
        else:
            return False

#Comparación genérica entre los datos de vectores
def comparar2 (vec1, vec2, v1inicio, v2inicio, posicion, tamaño):
    if posicion == tamaño:
        return True
    else: 
        d1=vec1[v1inicio + posicion]
        d2=vec2[v2inicio + posicion]
        if d1==d2:
            return comparar2(vec1,vec2, v1inicio, v2inicio,posicion+1,tamaño)
        else:
            return False


def subvectAux (minivec,vec,indice):
    if (len(vec)-len(minivec))+1 ==indice:
        return False
    else:
        hasta=indice+len(minivec)
        espaso=comparar(minivec, vec[indice:hasta],0)
        # == es equivalente a la función comparar        
        if espaso:
            return True
        else:
            return subvectAux(minivec,vec,indice+1)
        
        
def subvector (minivec, vec):
    if len(minivec) > len(vec):
        return False
    else:
        return subvectAux(minivec,vec,0)
    
##########################################
#5
def prod_escalarM_aux(escalar,M,filas,cols, i, j):
    if i == filas: #Ya se recorrieron todas las filas
        return M
    elif j == cols: #Ya se recorrió una fila
        return prod_escalarM_aux(escalar,M,filas, cols, i+1, 0) # Se pasa a la próxima fila
    else:
        elemento = M[i][j]  #Elemento (i,j) de la matriz
        M[i][j] = elemento * escalar
        return prod_escalarM_aux(escalar,M,filas, cols, i, j+1 ) #Se pasa al siguiente elemento
    
def prod_escalarM(e,M):
    filas = len(M)
    cols = len(M[0])
    return prod_escalarM_aux(e,M,filas, cols, 0, 0)


##########################################
#6
def muestreMAux(resultado,M,filas,cols, i, j):
    if i == filas: #Ya se recorrieron todas las filas
        return resultado
    elif j == cols: #Ya se recorrió una fila
        resultado += "\n"
        return muestreMAux(resultado,M,filas, cols, i+1, 0) # Se pasa a la próxima fila
    else:
        elemento = M[i][j]  #Elemento (i,j) de la matriz
        resultado += str(elemento) + " "
        return muestreMAux(resultado,M,filas, cols, i, j+1 ) #Se pasa al siguiente elemento
    
def muestreM(M):
    filas = len(M)
    cols = len(M[0])
    resultado = muestreMAux("",M,filas, cols, 0, 0)
    print (resultado)


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

##########################################
#7
def diagonalAux(matriz, filas, i, resultado):
    if i==filas:
        return resultado
    else: 
        elemento= matriz[i][i]
        resultado.append(elemento)
        return diagonalAux(matriz, filas, i+1, resultado)
 

def diagonal(matriz):
    filas= len(matriz)
    return diagonalAux(matriz, filas, 0, [])


##########################################
#8
def promedioAux (mat, n, m, i, j, resultado):
    if n==i:
        tamaño=n*m
        return (resultado/tamaño)
    elif m==j:
        return promedioAux (mat, n, m, i+1, 0, resultado)
    else: #en la misma fila
        elemento=mat[i][j]
        resultado += elemento
        return promedioAux (mat, n, m, i, j+1, resultado)
    
def promedio(mat):
        return promedioAux(mat,len(mat),len(mat[0]),0,0,0)



'''
6a.9
Escriba una función recursiva llamada mayor_xcol(mat) que recibe
    una matriz de tamaño nxm, devuelva el elemento mayor, haciendo el recorrido por columnas de la matriz original.
'''
 

def mayor_xcol_aux(mat, n, m, i, j, mayor):
    if m==j:
        return mayor
    elif n==i:#cambio de columna
        return mayor_xcol_aux(mat,n,m,0,j+1, mayor)
    else: #en la misma columna
        elemento=mat[i][j]
        if elemento>mayor:
            mayor=elemento            
        return mayor_xcol_aux(mat,n,m,i+1,j, mayor)
    
def mayor1_xcol(mat):
    return mayor_xcol_aux(mat,len(mat),len(mat[0]),0,0,mat[0][0])
    

    
m1 = [[1,2,7],[2,8,6],[9,4,6]]
prod_escalarM(-1,m1)
m2 = [[1,2,7],[2,8,6],[9,4,6]]


'''
Extra:

Escriba una función recursiva llamada mayores_col(mat) que recibe
    una matriz de tamaño nxm, devuelva una lista con los elementos mayores de
    cada columna, haciendo el recorrido por columnas de la matriz original.
'''
 

def mayores_col_aux(mat, n, m, i, j, mayor, lista):
    if (m-1==j) and (n==i) :#Para el últmo elemento
        lista.append(mayor)
        return lista
    elif n==i:#cambio de columna
        lista.append(mayor)
        return mayores_col_aux(mat,n,m,0,j+1, mat[0][j+1], lista)

    else: #en la misma columna
        elemento=mat[i][j]
        if elemento>mayor:
            mayor=elemento            
        return mayores_col_aux(mat,n,m,i+1,j, mayor, lista)
    
def mayores_col(mat):
    return mayores_col_aux(mat,len(mat),len(mat[0]),0,0,mat[0][0], [])
    

