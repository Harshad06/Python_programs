import monk

def func2():
    print("func2")

obj = monk.A()
obj.func1 = func2
obj.func1()