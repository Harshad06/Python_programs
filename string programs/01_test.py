'''
s = "Hello"
print(type(s))

print(s.__getitem__(0))
print(s.__getitem__(3))

print(s[3])

print(~4)
print(~~4)

a = 5
b = 3
print(a//b)

# in = 5 

#print("Hello"+1+2+3)    # Error

print("1" == 1)  # False
'''

'''
f = lambda a: a*f(a-1) if (a>1) else 1
#call lambda function
result = f(5)
print(result)
'''
'''
f = lambda n:1 if n==0 else n*f(n-1)
print(f(5))
'''