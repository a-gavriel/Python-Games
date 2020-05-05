def listas_iguales (L1,L2, contador, contador2):
  if (contador == len(L1)):
    return True
  else:
    elementoL1= L1 [contador]
    elementoL2= L2 [contador2]
    if (elementoL1==elementoL2):
      return listas_iguales (L1,L2, contador+1, contador2+1)
    else:
      return False

      
      

def subvector (vect1,vect2, contador2):
  if (contador2==len(vect2)-len(vect1)+1):
    return False
  else:
    soniguales = listas_iguales (vect1,vect2,0,contador2)
    if (soniguales):
      return True
    else:
      return subvector (vect1,vect2, contador2+1)
    
  
def muestreM_aux(matriz,i,j, string):
  if i == len(matriz):
    print( string)
  elif j == len(matriz[i]):
    string = string + "\n"
    return muestreM_aux(matriz,i+1,0, string)
  else:
    elemento = matriz[i][j]
    #print("El elemento en",i,j, "es", elemento)
    string = string + str(elemento)  + " "
    return muestreM_aux(matriz,i,j+1, string)
    

  
def muestreM(matriz):
  return muestreM_aux(matriz, 0,0, "" )
