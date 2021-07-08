
# Return thrice time value

def thrice(func):
    def inner(x,y):
        return 3*func(x,y)
    return inner

@thrice
def add(x,y):
    return x+y

print(add(5,6))        # 33