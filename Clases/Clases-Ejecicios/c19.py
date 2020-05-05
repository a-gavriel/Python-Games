def f(x=4,y=2, z=1):
  print(x, y, z)

"""
Programación Orientada a Objetos - OOP

Clases -> objetos

Atributos: características
Métodos: funciones


"""

class Carro:
  def __init__(self, marca, modelo, color = "Negro"):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.posicion = 0
    self.velocidad = 0
  def acelerar(self, cantidad):
    self.velocidad += cantidad
  def moverse(self):
    self.posicion += self.velocidad

c1 = Carro("BMW", "X6")
c2 = Carro("Jeep", "CJ7", "Azul")


class Mascota:
  def __init__(self,color,tamaño,nombre,edad = 0):
    self.color = color
    self.tamaño = tamaño
    self.edad = edad
    self.nombre = nombre
  def jugar(self):
    print(self.nombre,"está jugando")
  def getEdad(self):
    return self.edad
  def setEdad(self,edad):
    self.edad = edad



m1 = Mascota("café", "pequeño", "Jack", 8)


class Perro(Mascota):
  def __init__(self,color, tamaño, nombre, edad,raza):
    super().__init__(color,tamaño,nombre,edad)
  def ladrar(self):
    print("Guau! Guau!")



p1 = Perro("café", "pequeño", "Jack", 8, "Doberman")







