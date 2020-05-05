


def while1():
  x = 0
  while(x<10):
    if (x%2==1):
      print("impar", x )
    else:
      print("par", x )
    x += 1
  print("Fin")
  

def while2():
  L1 = [1,2,3,4,7]
  size1 = len(L1)
  i= 0
  while(i< size1):
    elemento = L1[i]
    L1[i] = elemento + 1
    print("indice",i,"=",elemento)
    i += 1
  print(L1)


##########################



def for1():
  L1 = [1,2,3,4,7]
  for elemento in L1:
    print(elemento,elemento*2)

def for2():
  STR = "Esto es texto."
  for char in STR:
    print(char)


def for3():
  L1 = [11,12,13,14,17]
  size = len(L1)
  # size = 5
  # range(5) va del 0 al 4
  for i in [0,1,2,3,4]:
    print(i)
    
  print("")
  
  for i in range(size):
    print("indice",i,"=",L1[i])
    L1[i] += 1
  print(L1)


def suma_impar(num):
  
  resultado = 0  
  while( num != 0 ):
    ultimo = num % 10
    if ultimo % 2 == 1:
      resultado += ultimo #resultado=resultado + ultimo
    num //= 10

  return resultado


def revise_num(num):
  menores = 0
  mayores = 0
  while( num != 0 ):
    ultimo = num % 10
    if ultimo < 5:
      menores += 1
    else:
      mayores += 1
      
    num = num // 10

  return menores,mayores
  


########################
def factorial_p(num):
  if num == 0:
    return 1
  else:
    return num * factorial_p(num-1)

########################
def factorial_c_aux(num,resultado):
  if num == 0:
    return resultado
  else:
    resultado = num * resultado
    num = num - 1
    return factorial_c_aux(num,resultado)

def factorial_c(num):
  return factorial_c_aux(num,1)


def factorial_i(num):
  resultado = 1
  while(num != 0):
    resultado = resultado * num
    num = num - 1
  return resultado
  
    

def hay_par(num):    
    while (num!=0):
        ultimo= num%10
        num//=10
        if ultimo%2==0:
            return True        
    return False

"""
Haga una funcion cuenta_par(lista) que reciba una lista y cuente la cantidad
  de números pares en la lista
"""

L1 = [1,2,3,4,7]

def cuenta_par(lista):
  resultado = 0
  
  for num in lista:
    if num % 2 == 0:
      resultado += 1

  return resultado

"""
Haga una funcion reemplazar(string,char1, char2) que reemplace cada ocurrencia
  del caracter char1 con el caracter char2

>>> reemplazar( 'Hola!', 'a' , 'i'   )
'Holi!'

"""

STR = "ABCBC"

def reemplazar(string,char1, char2):
  tamaño = len(string)
  nuevo = ""
  for i in range(tamaño):
    actual = string[i]
    
    if actual == char1:
      nuevo += char2
    else:
      nuevo += actual
  return nuevo
    

def palindromo(string):

  string = reemplazar(string," ","")
  while string != "":
    primero = string[0]
    ultimo = string[-1]
    if primero != ultimo:
      return False
    string = string[1:-1]

  return True


def prod_vector(v,w):
    tamaño=len (v)
    producto = 0
    for i in range (tamaño):
        actualv=v[i]
        actualw=w[i]
        producto += actualv*actualw
    return producto

def prod_vector_w(v,w):
    sizev = len(v)
    sizew = len(w)
    if sizev != sizew:
      return False
    producto = 0
    i = 0
    while(i < sizev):
      actualv = v[i]
      actualw = w[i]
      producto += actualv * actualw        
      i += 1
    return producto


  #############








