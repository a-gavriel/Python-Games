'''
Cálculo de e utilizando serie de Taylor
'''

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
##############################################
# Aproximando infinito con 10
def e10(n):
    if n>10:
        return 0
    else:
        step = 1/fact(n) 
        return step + e10(n+1)


##############################################
# Cálculo hacia abajo especificando el n máximo
def e(n):
    if n<0:
        return 0
    else:
        step = 1/fact(n)
        return step + e(n-1)

##############################################
# Cálculo hacia abajo especificando
#       el límite superior en el parámetro f
def eArriba(n,f):
    if n > f:
        return 0
    else:
        step = 1/fact(n)
        return step + eArriba(n+1,f)
    

##############################################
# Solución utilizando sumatoria y una función como parámetro
def Taylor(n):
    return 1/fact(n)

def sumatoria(i,f,fun):
    if i > f:
        return 0
    else:
        step = fun(i)
        return step + sumatoria(i+1,f,fun)





##############################################

'''
4b.5
Esciba una funcion suma_parimpar que reciba un número entero y retorne una
    tupla que tenga la siguiente forma:
    (suma-digitos-pares , suma-digitos-impares)

>>> suma_parimpar( 1564 )
( 10, 6 )

>>> suma_parimpar( 64 )
( 10, 0 )

'''    
def suma_aux(numero, paridad):
    if (numero == 0):
        return 0
    else:
        ultimo = numero % 10
        recortado = numero // 10
        if (ultimo % 2 == paridad):
            return ultimo + suma_aux(recortado, paridad)
        else:
            return suma_aux(recortado, paridad)



def suma_parimpar(numero):
    par = suma_aux(numero,0)
    impar = suma_aux(numero,1)
    return (par,impar)



'''
4b.6
>>> suma_divisores(6)
1+2+3 = 6

>>> suma_divisores(10)
1+2+5 = 8

''' 

def suma_divisores(i,f):
    if (i==f):
        return True
    else:
        residuo = f % i
        if (residuo == 0):
            return False
        else:
            return suma_divisores(i+1 , f)

'''
Haga un programa recursivo que determine si un número es primo

>>> primo(13)
True

>>> primo(8)
False
'''


def primo(numero):
    suma = suma_divisores(2,numero)
    return suma 



'''
4c.1
Escriba una función booleana mas_nueve(num) que recibe un número entero y
    verifica si el número dado tiene más de nueve dígitos.
>>> mas_nueve(1234567890)
True
>>> mas_nueve(2134)
False

'''
    
def suma(numero):
    if (numero == 0):
        return 0
    else:
        ultimo = numero % 10
        recortado = numero // 10
        return ultimo + suma(recortado)

def contar(numero):
    if (numero == 0):
        return 0
    else:
        recortado = numero // 10
        return 1 + contar(recortado)

def mas_nueve(numero):
    return contar(numero)>9
