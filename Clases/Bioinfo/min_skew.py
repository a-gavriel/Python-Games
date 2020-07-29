import random
d = {"A":0,"C":-1,"G":1,"T":0}
dna = [random.choice("ACGT") for _ in range(10)]
def getval(lst):
  val = 0
  for bp in lst:
    val += d[bp]
    yield val

skew = [val for val in getval(dna)]
