

###########################################
# 1
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
# 2
def cuente_par(num):
	if num == 0:
		return 0
	else:
		dig = num%10
		if dig%2 == 0:  #if  num%2 == 0:
			return 1 + cuente_par(num//10)
		else:
			return cuente_par(num//10)
###########################################
# 3
def primer_dig(num):
	recortado  = num//10
	if recortado == 0:
		return num
	else:
		return primer_dig(recortado)

def iguales(num):
	ultimo = num%10
	primer = primer_dig(num)
	return ultimo == primer


###########################################
# 4
def suma_dig(num):
	if num == 0:
		return 0
	else:	
		dig = num%10
		return dig + suma_dig(num//10)	

def suma10(num):
	suma = suma_dig(num)
	return suma >= 10


###########################################
# 5
def cuente_dig(num,dig):
	if num == 0:
		return 0
	else:
		ultimo = num%10
		if ultimo == dig:
			return 1 + cuente_dig(num//10,dig)
		else:
			return cuente_dig(num//10,dig)






###########################################
# 6
def revise_aux_H(num):
	if num == 0:
		return 0
	else:
		ultimo = num%10
		if ultimo > 4:
			return 1 + revise_aux_H(num//10)
		else:
			return revise_aux_H(num//10)

def revise_aux_L(num):
	if num == 0:
		return 0
	else:
		ultimo = num%10
		if ultimo < 5 :
			return 1 + revise_aux_L(num//10)
		else:
			return revise_aux_L(num//10)

def revise_num(num):
	mayores = revise_aux_H(num)
	menores = revise_aux_L(num)
	return (menores , mayores)


###########################################
# 7
def todos_pares(num):
	if num == 0:
		return True
	else:	
		dig = num%10
		if dig%2 == 1: # if num%2 == 1
			return False
		else:
			return todos_pares(num//10)


###########################################
# 8
def hay_par(num):
	if num == 0:
		return False
	else:	
		dig = num%10
		if dig%2 == 0:
			return True
		else:
			return hay_par(num//10)



###########################################

