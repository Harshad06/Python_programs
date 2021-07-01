
# ALL PATTERNS:-

'''
for row in range(5):
    for col in range(row+1):
        print("*", end="")
    print()

output:
*
**
***
****
*****

'''




'''
n=5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col, end="")
    print()

output:
12345
1234
123
12
1

'''





'''
n=5

for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row, end="")
    print()

output:
55555
4444
333
22
1

'''






'''
n=5 

for row in range(n,0,-1):
    for col in range(1, row+1):
        print(row, end="")

output:
555554444333221
'''




'''
mystr = 'HELLO'
num = len(mystr)

for row in range(num):
    for col in range(row+1):
        print(mystr[col], end="")
    print()

output:
H
HE
HEL
HELL
HELLO


'''





'''
n=5
num=1

for row in range(n):
    for col in range(0,row+1):
        print(num, end=" ")
        num+=1
    print()


output:
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15

'''





'''
n=5

for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()


output:
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5


'''





'''
n=5

for row in range(1, n+1):
    for col in range(1, row+1):
        print(row, end=" ")
    print()

output:
1 
2 2 
3 3 3
4 4 4 4
5 5 5 5 5

'''






'''
n=5

for row in range(n,0,-1):
    for col in range(1, row+1):
        print("*", end="")
    print()

output:
*****
****
***
**
*

'''