'''
Realizar una funcion que me retorne si el
    último digito de un numero entero
    es menor a 5, igual a 5 o mayor a 5.
Debe verificar que la entrada sea un numero entero

Hint: Puede utilizar la función módulo con 10.
    Ejemplo 23 % 10 = 3
'''
def comparacion_aux(numero):
    udigito = numero % 10
    if (udigito == 5):
        return "El último dígito es igual a 5"
    elif (udigito > 5):
        return "El último dígito es mayor a 5"
    elif (udigito  < 5):
        return "El último dígito es menor a 5"
    else:
        return "Entrada inválida"


def comparacion(numero):
    if (isinstance(numero,int)):
        return comparacion_aux(numero)
    else:
        return "Entrada inválida"


'''
Escriba un programa en Python que reciba un número entero
    positivo de un máximo de 5 dígitos e indique si el
    primer dígito y el último dígo son iguales
    >>> iguales(4)
    True
    >>> iguales(464)
    True
'''
def iguales(numero):
    if (not isinstance(numero,int)):
        return "Entrada inválida"
    elif numero < 0:
        return "Entrada inválida"
    elif numero < 10: #El número tiene 1 dígito
        return True
    elif numero < 100:#El número tiene 2 dígitos
        ultimo = numero % 10
        primero = numero // 10
        soniguales = ultimo == primero
        return soniguales
    elif numero < 1000: #El número tiene 3 dígitos
        ultimo = numero % 10
        primero = numero // 100
        soniguales = ultimo == primero
        return soniguales
    elif numero < 10000:#El número tiene 4 dígitos
        ultimo = numero % 10
        primero = numero // 1000
        soniguales = ultimo == primero
        return soniguales
    elif numero < 100000:#El número tiene 5 dígitos
        ultimo = numero % 10
        primero = numero // 10000
        soniguales = ultimo == primero
        return soniguales
    else:
        return "Entrada inválida"
 

def iguales2(numero):
    if (not isinstance(numero,int)):
        return "Entrada inválida"
    elif numero < 0:
        return "Entrada inválida"
    else:
        sNumero = str( numero )
        primero = sNumero[0]
        ultimo = sNumero[-1]
        soniguales = primero == ultimo
        return soniguales


"""
Escriba un programa que reciba un número entero de 3
    dígitos y sume sus dígitos
"""

def suma (numero):
  ultimo = numero %10
  numero1= numero //10
  medio = numero1 %10
  primer = numero1 // 10
  suma = ultimo + medio + primer
  divisible = suma %2
  return divisible == 0
  

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial( n-1 )



def sumatoria(n):
    if(n == 0):
        return 0
    else:
        return n + sumatoria (n - 1)


def sumatoriaG(i,n):
    if(i == n):
        return n
    else:
        return i + sumatoriaG (i+1 , n)












