'''
4. Escriba una funcion llamada llave, que exprese la capacidad de una llave maya
en bytes, conociendo la capacidad de la llave en gigabytes. Considere que: 1
kilobyte = 1024 bytes, 1 megabyte = 1024 kilobytes, 1 gigabyte = 1024 megabytes.
'''

def llave (gigabytes):
    byte=gigabytes*(1024*1024*1024)
    return byte

'''
8. Escriba un programa que reciba un número entero de 3 dígitos 
e indique si la suma de sus dígitos es par.
'''
def par (digitos):
    if(digitos<1000 and digitos>99):
        a=str(digitos)
        d1=int(a[0])
        d2=int(a[1])
        d3=int(a[2])
        suma=d1+d2+d3
        residuo=suma%2
        espar= residuo == 0
        return espar
    else:
        return "Este numero no es válido"


def f():
    a = 4
    b = 5
    return a + b

def ejem():
    a = 1
    b = 2
    c = f()
    d = 3
    return d

def impar (digitos):
    if(digitos<1000 and digitos>99):
        d1=digitos%10
        cociente= digitos//10 
        d2=cociente%10
        d3= cociente//10
        suma=d1+d2+d3
        residuo=suma%2
        esimpar= residuo != 0
        return esimpar
    else:
        return "Este numero no es válido"
    
