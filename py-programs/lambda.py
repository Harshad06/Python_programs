
f = lambda x,y : x+y
print(f(4,5))

f = lambda x,y : x**y
print(f(2,2))

# Factorial
f = lambda n: 1 if n==0 else n*f(n-1)
print(f(5))

# max of x & y
max = lambda x,y: x if x>y else y
print(max(8,5))

