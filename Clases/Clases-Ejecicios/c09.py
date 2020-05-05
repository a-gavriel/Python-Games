def base2_10(num):
  if num == 0:
    return 0
  else:
    return num%10 + 2*base2_10(num//10)

def size(num):
  if num == 0:
    return 0
  else:
    return 1 + size(num//10)

def inv(num):
  if num == 0:
    return 0
  else:
    s = size(num)
    order = 10**(s-1)
    first = num //order
    res = num % order    
    return first + 10*inv(res)

def pal(num):
  if num == 0:
    return True
  else:
    s = size(num)
    order = 10**(s-1)
    first = num //order
    last = num % 10
    res = (num % order)//10
    if (first != last):
      return False
    else:
      return pal(res)

########################################################
    
def invertir(lista,resultado):
  if lista == []:
    return resultado
  else:
    resultado.append(lista[-1])
    return invertir(lista[:-1],resultado)

def invertir2(lista,resultado):
  if lista == []:
    return resultado
  else:
    resultado = [lista[0]] + resultado
    return invertir2(lista[1:],resultado)



###############################
'''
>>> divisores(6)
[1,2,3,6]

'''

def divisores(lista,num,divisor):
  if num == divisor: #num < divisor
    lista.append(num)
    return lista
  else:
    residuo = num % divisor
    if residuo == 0:
      lista.append(divisor) #lista = lista + [divisor]
    return divisores(lista,num,divisor + 1)
 

'''
Escriba una función que calcule la serie geométrica
  geométrica(a,n), con a un número real y n un número
  natural, utilizando:

 geométrica(a,n) = a**0 + a**1 + a**2 + ... + a**n


>>> geometrica(0.5,10)
0.5**0 + 0.5**1 + ... + 0.5**10 = 1.99804687

>>> geometrica(3,3)
3**0 + 3**1 + 3**2 + 3**3 = 40


'''

def geométrica_aux (a,n,contador,resultado):
  if n < contador: # if n == contador: 
    return resultado
  else:
    paso = a**contador # a**n
    return geométrica_aux(a,n,contador+1,resultado+paso)

def geométrica(a,n):
  return geométrica_aux(a,n,0,0)



'''
Escriba una funcion divida(dig,lista) que reciba un
  dígito y una lista y obtenga dos listas.
  - La primera compuesta por los dígitos mayores o iguales
    al dígito dado
  - La segunda compuesta por los dígitos menos al
    dígito dado
>>> divida(5, [1,2,3,5,6,1])
( [5,6] , [1,2,3,1] )

>>> divida( 3, [1,2,3,5,6,1])
( [3,5,6] , [1,2,1] )

    
'''

def dividaAux (dig,lista,resultado_mayores,resultado_menores):
  if lista==[]:
    return (resultado_mayores, resultado_menores)
  else:
    primero=lista[0]
    if (primero >=dig):
      resultado_mayores.append (primero)
    else:
      resultado_menores.append(primero)
    return dividaAux(dig,lista[1:],resultado_mayores,
                   resultado_menores)
    
def divida(dig,lista):
  return dividaAux(dig,lista,[],[])
      





