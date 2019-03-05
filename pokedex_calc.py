




def f(x):
 less  = x-1
 box = less //30 +1
 n = less % 30
 row = n //6 +1
 col = n %6 +1
 print ('box: ' + str(box) + ' - row: ' + str(row) + ' - col: ' + str(col))


def pk():
 x = 1
 while x!=0:
  raw = input()
  x = int(raw)
  f(x) 
