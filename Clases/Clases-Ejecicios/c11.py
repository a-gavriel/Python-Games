
def vector_invert_aux(v,cont_p, cont_n):
  if cont_p == len(v)//2:
    return v
  else:
    izq = v[cont_p]
    der = v[cont_n]
    v[cont_n] = izq
    v[cont_p] = der
    return vector_invert_aux(v,cont_p+1, cont_n-1)
    
def vector_invert(v):
  return vector_invert_aux(v,0,-1)

##############################

def prod_escalar_aux (e,v,contador):
  if (contador == len(v)):
    return v
  else:
    elemento = v[contador]
    producto = elemento*e
    v[contador] = producto
    return prod_escalar_aux (e,v, contador + 1)

def prod_escalar(e,v):
  return prod_escalar_aux(e,v,0)


##############################

def prod_vector_aux (v,w,contador,resultado):
  if (contador == len(v)):
    return resultado
  else:
    elementov= v[contador]
    elementow= w[contador]
    producto= elementov*elementow
    resultado= resultado + producto
    return prod_vector_aux (v,w,contador+1,resultado)

def prod_vector(v,w):
  if len(v) == len(w):
    return prod_vector_aux(v,w,0,0)


##############################
