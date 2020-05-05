def tiene3(numero):
    if isinstance(numero,int):
        return tiene3_aux(numero)
    else:
        return "Entrada inválida"

def tiene3_aux(numero):
    if (numero == 0):
        return False
    else:
        ultimo = numero % 10
        if (ultimo == 3):
            return True
        else:
            numero_recortado = numero // 10
            return tiene3(numero_recortado)


def sumatoria(numero):
    if (numero == 0):
        return 0
    else:
        return numero + sumatoria(numero - 1)

'''
Haga una funcion recursiva que sume los digitos
    de un número entero. No necesita hacer validaciones

>>> suma(123)
6

>>> suma(1234)
10
'''
def suma(numero):
    if (numero == 0):
        return 0
    else:
        ultimo = numero % 10
        recortado = numero // 10
        return ultimo + suma(recortado)


'''
Haga una funcion recursiva que cuente los dígitos de
    un número entero. No necesita hacer validaciones.
>>> contar(11)
2
>>> contar(222)
3
'''
def contar(numero):
    if (numero == 0):
        return 0
    else:
        recortado = numero // 10
        return 1 + contar(recortado)

#Calculo de fibonacci
def fibonacci(num):
    if(num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)



def productoria(i,f):
    if (i==f):
        return i
    else:
        return i* productoria(i+1,f)



















            

