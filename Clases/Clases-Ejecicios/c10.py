
'''
Escriba una función largo(num) que recibe un número
  entero y retorna la cantidad de dígitos del número.


'''
def largo_aux(num, resultado):
  if num == 0:
    return resultado
  else:
    return largo_aux(num//10,resultado+1)

def largo(num):
  return largo_aux(num,0)
'''
###############################
Escriba una función primer(num,cantidad_dig) que retorna
  el primer dígito del número a partir de la cantidad de
  dígitos del número calculado en la función anterior
Recuerde que:
  234 // 100 = 2   \  100 = 10**2
  4321 // 1000 = 4  \  1000 = 10**3

'''
def primer(num):
  cantidad_dig = largo(num)
  exp = 10**(cantidad_dig-1)
  return num // exp

def primer2(num):
  if num < 10:
    return num
  else:
    return primer2(num//10)


'''

###############################

Escriba una función genere(lista) que recibe una lista
  de dígitos y retorna el número generado por dichos
  dígitos

>>> genere( [1,0,1,5] )
1015


a = 93
b = 1

c = 931  \  c = a*10 + b

>>> genere( [3,5,1] )
351
''' 

def genere_aux(lista,resultado):
  if lista == []:
    return resultado
  else:
    primer = lista[0]
    resultado = resultado*10 + primer
    return genere_aux(lista[1:],resultado)

def genere(lista):
  return genere_aux(lista,0)


'''
Escriba una funcion palindromo(string) que reciba un
  string y retorne si es un palíndromo o no.

>>> palindromo("hola")
False

>>> palindromo("tacocat")
True
'''

def palindromo(string):
  if string == "":
    return True
  else:
    primer = string[0]
    ultimo = string[-1]
    if (primer == ultimo):
      return palindromo(string[1:-1])
    else:
      return False


def base_2(num, resultado):  
  if num < 2:
    resultado = str(num) + resultado 
    return resultado
  else:
    cociente = num // 2
    residuo = num % 2
    resultado = str(residuo) + resultado 
    #resultado = resultado * 10 + residuo #Para numeros
    return base_2(cociente, resultado)


def base_N(num, resultado, digito):  
  if num < digito:
    resultado = str(num) + resultado 
    return resultado
  else:
    cociente = num // digito
    residuo = num % digito
    resultado = str(residuo) + resultado 
    #resultado = resultado * 10 + residuo #Para numeros
    return base_N(cociente, resultado, digito)


def convierta(c):
  if c == "A":
    return 10
  elif c == "B":
    return 11
  elif c == "C":
    return 12
  elif c == "D":
    return 13
  elif c == "E":
    return 14
  elif c == "F":
    return 15
  else:
    return int(c)

def base10(num,base,exp,resultado):
  if num == "":
    return resultado
  else:
    ultimo = convierta(num[-1])
    paso = ultimo * (base**exp)
    return base10(num[:-1], base, exp+1, resultado + paso)


'''
haga una función mayor(lista) que me devuelva el mayor
  elemento de una lista de números enteros


''' 
def mayor_aux(lista, resultado):
  if lista ==[]:
    return resultado
  else:
    primero = lista [0]
    if (primero > resultado):
      resultado = primero
      return mayor_aux (lista [1:], resultado)
    else:
      return mayor_aux (lista [1:], resultado)
    

def mayor(lista):
  return mayor_aux(lista, lista[0])










