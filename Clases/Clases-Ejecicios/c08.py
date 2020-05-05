        
###########################################
'''
4b.7
'''

def contiene(num,dig):
    if num == 0:
        return False
    else:
        ultimo = num%10
        if (ultimo == dig):
            return True
        else:
            return contiene(num//10,dig)

def dig_ab(A,B):
    if A == 0:
        return True
    else:
        ultimo = A % 10
        ultimo_en_B = contiene(B,ultimo)
        if ultimo_en_B:
            return dig_ab(A//10,B)
        else:
            return False
        
###########################################

def suma_impar(num):
	if num == 0:
		return 0
	else:	
		dig = num%10
		if dig%2 == 1:
			return dig + suma_impar(num//10)
		else:

			return suma_impar(num//10)
		    
###########################################




def suma_imparC_aux(num,resultado):
    if num == 0:
        return resultado
    else:
        dig = num%10
        if dig % 2 == 1:
            # El resultado actualizado es
            #   el resultado anterior + dig
            return suma_imparC_aux(num//10,resultado + dig)
        else:
            return suma_imparC_aux(num//10,resultado)
    

def suma_imparC(num):
    return suma_imparC_aux(num,0)


###########################################

def cuente_dig_aux(num,resultado):
    if num == 0:
        return resultado
    else:
        return cuente_dig_aux(num//10, resultado + 1)

def cuente_dig(num):
    return cuente_dig_aux(num,0)

###########################################


def lenn(lista, resultado):
    if lista == []:
        return resultado
    else:
        return lenn(lista[1:],resultado + 1)

###########################################

def iota_aux(num,contador,resultado):    
    if contador == num:
        return resultado
    else:        
        resultado.append(contador)
        print(resultado)
        return iota_aux(num,contador+1, resultado)
    
def iota(num):
    return iota_aux(num,0,[])


###########################################

def cuales_aux(num, resultado):
    if num == 0:
        return resultado
    else:
        ultimo = num%10
        if ultimo < 5:
            resultado =  [ultimo] + resultado
        return cuales_aux(num//10, resultado)
        
def cuales2_aux(num, resultado):
    if num == 0:
        return resultado
    else:
        ultimo = num%10
        if ultimo < 5:
            nuevo = [ultimo]
            nuevo.extend(resultado)
            return cuales2_aux(num//10, nuevo)
        else:
            return cuales2_aux(num//10, resultado)
        

def cuales(num):
    return cuales_aux(num, [])
        
###########################################


def eliminar_aux(lista, ele, resultado):    
    if lista == []:
        return resultado
    else:
        primer = lista[0]
        if primer != ele:
            resultado.append(primer)            
            return eliminar_aux(lista[1:], ele, resultado)
        else:
            return resultado + lista[1:]


def eliminar(lista,ele):
    return eliminar_aux(lista, ele, [])

###########################################

def eliminarTodos_aux(lista, ele, resultado):
    if lista == []:
        return resultado
    else:
        primer = lista[0]
        if primer != ele:
            #resultado = resultado + [primer]
            resultado.append(primer)            
        return eliminarTodos_aux(lista[1:], ele, resultado)


def eliminarTodos(lista,ele):
    return eliminarTodos_aux(lista, ele, [])

###########################################

'''

Hacer una función llamada invierta(lista), que reciba
    una lista e invierta el orden de sus elementos
    (sin utilizar la función reverse de Python)

>>> invierta([1,2,3,4,5])
[5,4,3,2,1]

'''

















