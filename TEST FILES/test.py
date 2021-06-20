'''
for row in range(0,5):
    for col in range(0,row+1):
        print("*", end=" ")
    print()
'''

'''
n = int(input("Enter a number: "))
num=1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(num, end=" ")
        num +=1
    print()
'''
'''
mystr = input("Enter the String :")
len = len(mystr)

for row in range(len):
    for col in range(0, row+1):
        print(mystr[col], end=" ")
    print()
'''

'''
f = lambda n:1 if n==0 else n*f(n-1)
print(f(6))
'''

'''
def isPalindrome(s):
    return s == s[::-1]

s = input("Enter the string :")
res = isPalindrome(s)

if res:
    print("Yes")
else:
    print("No")
'''

'''
def fibo(limit):
    a, b = 0, 1

    while(a<limit):
        yield a
        a, b = b, a+b

it = fibo(10)
fib = []
while True:
    try:
        fib.append(next(it))
    except StopIteration:
        break

print(fib)
'''

'''
def isPrime(n):
    for i in range(2,n):
        if not (n % i):
            return False
    return True

for n in range(1, 20):
    if isPrime(n):
        print(n, end=" ")
'''

'''
old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}

print(old_dict, end="\n")

new_dict = {}
for key, value in old_dict.items():
    if value in new_dict:
        new_dict[value].append(key)
    else:
        new_dict[value] = [key]

print ("Dictionary after swapping is : ")
print("keys: values")
for i in new_dict:
    print(i, " : ", new_dict[i])
'''

'''
def even_nos(n):
    i = 1
    while n:
        yield 2*i
        i+=1
        n-=1

it = even_nos(10)
even_list =[]

while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break

print(even_list)
'''


'''
lst = ["HARSHAD", "SHRINGI"]

rev_char = [x[::-1] for x in lst]
print(rev_char)

length = len(rev_char)

for i in range(length):
    print(rev_char[length-i-1], end=" ")
'''