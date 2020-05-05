from math import pi
from math import sqrt

def esfera(radio):
    PI = 3.141592
    vol = 4*pi*radio*radio*radio/4
    area = 4*pi*radio*radio
    return(vol , area)

def numeros(a,b,c,d,e):
    sum = a+b+c+d+e
    av = sum/5
    return sum,av

def romano(n):
    if n == 1:
        return "I"
    elif n == 2:
        return "II"
    elif n == 3:
        return "III"
    elif n == 4:
        return "IV"
    elif n == 5:
        return "V"
    elif n == 6:
        return "VI"
    elif n == 7:
        return "VII"
    else:
        return "Error"

def area(a,b,c):
    p = (a+b+c)
    s = p/2
    sq = s*(s-a)*(s-b)*(s-c)
    area = sq**(0.5)
    return p,area

def convertir(m,i):
    cm =  m*100
    inches = cm/2.54
    foot = inches/12
    yard = foot/3
    if i == 1:
        return  cm
    elif i == 2:
        return inches
    elif i == 3:
        return foot
    elif i == 4:
        return yard
    else:
        return "i not valid"

def calc_salario(h,price):
    if h <= 40:
        return price * h
    else:
        base = 40*price
        h -= 40
        extra = h*price*1.5
        return base + extra


def recomendation(age,sex):
    if age < 18:
        return "gaseosa"
    elif age < 60 and sex == "hombre":
        return "tequila"
    elif age < 60 and sex == "mujer":
        return "margarita"
    elif age >= 60 and sex == "hombre":
        return "lechita"
    elif age >= 60 and sex == "mujer":
        return "sustagen"
    else:
        return "Error en datos ingresados"

def vacaciones(casado, edad, salario, destino):
    if edad <= 21 and destino == "Las Vegas":
        return "debe ser mayor de edad"
    elif salario <= 1000 and destino == "Las Vegas":
        return "necesita más dinero"
    elif casado and destino == "Puntarenas" and salario >= 3000:
        return "Un destino más romántico podría ser Europa"
    else:
        return "Válido"

def iguales(n):
    n_str = str(n)
    last = n_str[-1]
    first = n_str[0]
    return last == first

def adjunto(num,dig):
    n_str = str(num)
    adj = n_str + str(dig)
    return int(adj)

def dv(i,r):
    if r < 0:
        return "La resistencia no debe ser negativa"
    elif r > 1000:
        return "La resistencia debe ser menor a 1000"
    else:
        v = i*r
        return v
















    