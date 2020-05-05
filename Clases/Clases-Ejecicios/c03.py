from math import sqrt

def area_circulo(radio):
    pi = 3.1415
    area = pi * radio * radio
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_triangulo(base,altura):
    area = base * altura / 2
    return area

def area_tri(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(0.5)
    return area
