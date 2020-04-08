from math import sqrt


# Esta funcion calcula las soluciones de una ecuacion cuadrática
'''
Esta funcion calcula las soluciones de una ecuacion cuadrática

Entradas:  3 números enteros o flotantes
Salida: 2 números flotantes o complejos
Restricciones: No funciona para el número 0
'''
def cuadratica(a,b,c):
    d = sqrt(b**2 + 4*a*c)    # Se calcula el discriminante
    x1 = (-b + d )/(2*a)    # se calcula la primera solucion
    x2 = (-b - d) /(2*a)    # segunda solucion.
    return x1,x2




"""
Esta funcion es un ejemplo para utilizar el debugger

"""
def funcion():
    a = 1
    b = 5
    c = 4
    x1, x2 = cuadratica(a,b,c)

    a = 1
    b = 2
    c = 1
    y1,y2 = cuadratica(a,b,c)
    
    return 0

#calcula el valor absoluto de un número
#entrada: numero
#salida: numero
def absoluto_aux(numero):
    esPositivo = numero >= 0
    if (esPositivo):
        return numero
    else:
        return -1 * numero

#valida la entrada con type
def absoluto1(numero):
    if (type(numero) == type (1)) or (type(numero)== type(1.1)):
        return absoluto_aux(numero)
    else:
        return "Entrada inválida"

#valida la entrada con isinstance
def absoluto2(numero):
    if isinstance(numero,int) or isinstance(numero,float):
        return absoluto_aux(numero)
    else:
        return "Entrada inválida"

#retorna el string de un digito del 1-4
def string(digito):
    if (digito == 1):
        return "uno"
    elif (digito == 2):
        return "dos"
    elif (digito == 3):
        return "tres"
    elif (digito == 4):
        return "cuatro"
    else:
        return "Entrada inválida"


def dobleif(digito):
    if (digito <= 2):
        print( "menor o igual a 2")
    elif (digito == 2):
        print( "dos")
    else:
        print( "Entrada inválida")


'''
Tarea:

Realizar una funcion que me retorne si el último digito de un numero entero
es menor a 5, igual a 5 o mayor a 5.
Debe verificar que la entrada sea un numero entero
Hint: Puede utilizar la función módulo con 10. Ejemplo 23 % 10 = 3

'''






    
