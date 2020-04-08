class node:
    def __init__(self, data=""):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode
        self.size += 1
    def printL(self):
        print ("Printing Stack")
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next
    def pop(self):
        if self.size != 0:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value
        else:
            return -1


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add1(self,data):
        self.size += 1
        if self.size != 0:        
            current = self.head
            while(current.next != None):
                current = current.next
            newNode = node(data)
            current.next = newNode
            self.tail  = newNode
        else:
            newNode = node(data)
            self.head = newNode
            self.tail = newNode
    def add2(self,data):
        if self.size != 0:
            newNode = node(data)
            self.tail.next = newNode
            self.tail = newNode 
        else:
            newNode = node(data)
            self.head = newNode
            self.tail = newNode
        self.size += 1
    def printL(self):
        print ("Printing Queue")
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next
    def pop(self):
        if self.size != 0:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value
        else:
            return -1


'''

LL = Queue()
LL.add2("10")
LL.add2("11")
LL.add2("12")
LL.printL()
a = LL.pop()
LL.printL()
print("a=",a)

'''

class Vector:
    def __init__ (self, data=[]):
        self.data = data
        self.size = len(data)
    def __add__(self, v2):
        s1 = len(self.data)
        s2 = len(v2.data)
        if  s1 == s2:
            result = [0]*s1
            for i in range (s1):
                result [i] = self.data[i] + v2.data[i]
            return result
        else:
            return -1
    def __mul__(self, v2):
        s1 = len(self.data)
        s2 = len(v2.data)
        if  s1 == s2:
            result = 0
            for i in range (s1):
                result += self.data[i] * v2.data[i]
            return result
        else:
            return -1
    
def generate(rows,cols):
        result = []
        for i in range(rows):
            result.append ( [0]*cols )
        return result      

def sumaM(M1,M2):
        rows1 = len(M1)
        rows2 = len(M2)
        cols1 = len(M1[0])
        cols2 = len(M2[0])
        if (rows1 == rows2) and (cols1 == cols2):
            R = generate(rows1,cols1)
            for i in range(rows1):
                for j in range(cols1):
                    R[i][j] = M1[i][j] + M2[i][j]     
            return R
        

def multM(M1,M2):
        rows1 = len(M1)
        rows2 = len(M2)
        cols1 = len(M1[0])
        cols2 = len(M2[0])
        if (cols1 == rows2):
            R = generate(rows1,cols2)
            for i in range(rows1):
                for j in range(cols2):
                    dot = 0
                    for k in range(rows1):
                        dot += M1[i][k] *M2[k][j]
                    R[i][j] = dot
            return R
        

class complejo:
    def __init__(self,a,b):
        self.r = a
        self.i = b
    
    def __add__(self,X):
        Real = self.r + X.r
        Imaginaria = self.i + X.i
        return (Real,Imaginaria)

    def __mul__(self,X):
        Real = self.r * X.r - self.i * X.i
        Imaginaria = self.r * X.i + self.i * X.r
        return (Real,Imaginaria)

    def magnitud(self):
        None
    
    

c1 = complejo(1,2)
c2 = complejo(3,4)
print (c1*c2)



V1 = Vector([1,2])
V2 = Vector([1,2])

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = multM(A,B)
#print(C)