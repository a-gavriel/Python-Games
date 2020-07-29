#f1
def area_rect(length, width):
    area = length * width
    return  area

#2
def col_to_usd(cols):
    usd = cols/566
    return usd
#3
def usd_to_col(usd):
    col = usd*566
    return col

def toC(F):
    C = (F-32)/9*5
    return C
    
def toF(C):
    F = C/5*9 + 32
    return F

def toB(GB):
    MB = GB * 1024
    KB = MB * 1024
    B = KB * 1024
    return B

def average5(a,b,c,d,e):
    sum = a+b+c+d+e
    av = sum/5
    return av

def a_p_rect(length,width):
    area = length * width
    perimeter = 2*(length + width)
    return (area,perimeter)

def sum3(n):
    n1 = n%10
    n = n//10
    n2 = n%10
    n = n//10
    n3 = n%10
    sum_ = n1 + n2 + n3
    return sum_

def par(N):
    sum = sum3(N)
    return sum%2 == 1
    