'''
class Test:
    h = 10
    _h = 20
    __h = 30

class B(Test,Test2):
    pass
print(Test.h)
print(Test._h)
print(Test._Test__h)
'''
'''
class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")
        
    def display2(self):
        print("Class B")

class C(A):
    def display(self):
        print("Class C")
  
class D(B,C):
    
    def __init__(self):
                  
        self.display()

D()
'''
'''
def my_method(no_1, no_2):
    pass

def my_method(no_1, no_2, no_3):
    pass
    
my_method(1,2)
'''
'''
def prime_no(n):
    for i in range(2,n):
        if not (n%i):
            return False
    return True

def generatePrime(num):
    for n in range(num):
        if prime_no(n):
            yield(n)
    
for n in generatePrime(30):
    print(n)
'''
'''
def divide(no_1,no_2):
    if (no_2 > no_1):
        no_1,no_2 = no_2, no1


@divide
def div(no_1, no_2):
    return no_1/no_2

print(div(4,2))
print(div(2,4))
'''
'''
def inc(x):
    return x+1

def xyz(func, x):
    res = func(x)
    return res
'''

'''
Pavan, 5:16 PM
class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")
        
    def display2(self):
        print("Class B")

class C(A):
    def display(self):
        print("Class C")
  
class D(B,C):
    
    def __init__(self):
        if <condition>:
            self.display()
            
        self.display()

D()

Pavan, 5:23 PM
def my_method(no_1, no_2):
    pass

def my_method(no_1, no_2, no_3):
    pass
    
my_method(1,2,3)

Pavan, 5:38 PM
def div(no_1, no_2):
    return no_1/no_2

div(4,2) => 2

div(2,4) => 2

0.5
'''