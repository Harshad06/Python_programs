
#print(r"\nhello")

'''
ex = "snow flake"
ex[3] = 's'
print(ex)
'''

# print("hello"+1+2+3)

'''
i, j = 5, 4
print(i.__add__(j))
'''
'''
print('*',"abcdef".center(7),'*')
print('*',"abcdef".center(6),'*')
print('*',"abcdef".center(8),'*')
print('*',"abcdef".center(9),'*')
print('*',"abcdef".center(10),'*')
print('*',"abcdef".center(5),'*')
'''

#print("xyyzyxyzyxyy".count('xyy',2,11))

'''
print('a'.maketrans('ABC','123'))
print('b'.maketrans('ABC','123'))
print('x'.maketrans('DEF','123'))
print('x'.maketrans('DEF','456'))
print('a'.maketrans('abc','123'))
'''

'''
t = 32.00
[round((x-32)*5/9) for x in t]    #'int' and 'float' object is not iterable
'''

#print([i.lower() for i in "HELLO"]) 

'''
list1 =[1,3,2]
print(list1*2)      # [1, 3, 2, 1, 3, 2]
print(list1**2)     # unsupported operand type(s) for ** or pow(): 'list' and 'int'
'''
'''
l1 =[1,3,2]
print(l1)                   # [1, 3, 2]
print([x*2 for x in l1])    # [2, 6, 4]
'''

#print("welcome to python".split())  #['welcome', 'to', 'python']

# set()   # to create an empty set

'''
s = {san}   #NameError: name 'san' is not defined
s = {abs}
'''

'''
print(round(4.5676,1))      # 4.6
print(round(4.5676,2))      # 4.57
print(round(4.5676,3))      # 4.568
print(round(4.5676,4))      # 4.5676
'''

'''
print(hex(0))     # 0x0
print(hex(9))     # 0x9
print(hex(10))    # 0xa
print(hex(15))    # 0xf
print(hex(16))    # 0x10
print(hex(25))    # 0x19
print(hex(26))    # 0x1a
print(hex(31))    # 0x1f
print(hex(32))    # 0x20
'''

#print(22%3)  # 1

#print(3*1**3)   #3

#print(round())     #error
#print(round(48.5))  #48

'''
print(round(0.5)-(round(-0.5))) #0
print(round(0.5))   #0
print(round(0.6))   #1
print(round(1.6))   #2
print(round(1.5))   #2
print(round(1.4))   #1
print(round(0.50))  #0
print(round(0.51))  #1
'''

'''
abc = 1,000,000
#a b c = 1000 2000 3000
a,b,c = 1000, 2000, 3000
a_b_c = 1,000,000

print(abc)
#print(a b c)
print(a,b,c)
print(a_b_c)
'''

'''
print(bin(10-2)+bin(12^4))
print(bin(10-2))
print(bin(12^4))
'''

'''
print("The {} of my life".format('LOVE'))
print("{1} is the {0} side of life".format('bright','Happiness'))
'''

'''
x=56.236
print("%.2f"%x)     #56.24
print("%.1f"%x)     #56.2
print("%f"%x)       #56.236000
print("%d"%x)       #56
'''

# print("%-ns"%S)  # to add a 'n' blank space after a given string S

'''
i=2
while True:
    if i%3==0:
        break
    print(i)
    i+=2
'''

'''
x = "abcdef"
i = "i"
while i in x:
    print(i, end=" ")
'''

'''
for i in range(float('inf')):
    print(i)
# TypeError: 'float' object cannot be interpreted as an integer
'''

#print(0.1 + 0.2 == 0.3)  # False
'''
print(~4)       # -5
print(~~~~~~5)  # 5
print(~~~~~~~5) #-6
'''
'''
a=3
b=1
print(cmp(a,b))
'''

"""
for i in range(0, 5):
    print(i, end="\n")
"""
