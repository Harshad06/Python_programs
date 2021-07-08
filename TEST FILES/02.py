
# Return sum three times

def thrice(func):
    def inner(x,y):
        n=3
        while n>0:
            print(func(x,y))
            n-=1
    return inner

@thrice
def add(x,y):
    return x+y

add(5,6)

'''
output:

11
11
11
'''