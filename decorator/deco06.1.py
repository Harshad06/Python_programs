
def smart_divide(func):
    def inner(a,b):
        if (b>a):
            a,b = b,a
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

print(divide(4,2))
print(divide(2,4))