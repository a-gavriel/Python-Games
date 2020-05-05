def base2_10(num):
  if num == 0:
    return 0
  else:
    return num%10 + 2*base2_10(num//10)

def size(num):
  if num == 0:
    return 0
  else:
    return 1 + size(num//10)

def inv(num):
  if num == 0:
    return 0
  else:
    s = size(num)
    #se puede optimizar ya que el orden siempre disminuye en 1
    order = 10**(s-1) 
    first = num //order
    res = num % order    
    return first + 10*inv(res)

def pal(num):
  if num == 0:
    return True
  else:
    s = size(num)
    order = 10**(s-1)
    first = num //order
    last = num % 10
    res = (num % order)//10
    if (first != last):
      return False
    else:
      return pal(res)


def invertir(lista,resultado):
  if lista == []:
    return resultado
  else:
    resultado.append(lista[-1])
    return invertir(lista[:-1],resultado)

def invertir2(lista,resultado):
  if lista == []:
    return resultado
  else:
    resultado = [lista[0]] + resultado
    return invertir2(lista[1:],resultado)


