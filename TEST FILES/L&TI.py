'''
peak find length??
lst = [3,2,4,6,5,9,12,10]



sum 10 for any 2 numbers??
l1 = [3,2,4,6,5,9,12,10]




def thrice(func):
    def inner(x,y):
        n=3
        while n>0:
            print(func(x,y))
            n-=1
        #return 3*func(x,y)
    return inner

@thrice
def add(x,y):
    return x+y

add(5,6)
'''


class Animal():
    def speak(self):
        print(f'Animal is speaking')

class Mammal():
    def speak(self):
        print(f'Mammal is speaking')

class Dog(Animal,Mammal):
    pass 

obj = Dog()
print(obj.speak())