
n=5

for r in range(1,n+1):
    for sp in range(n,r,-1):
        print(" ", end="")
    for c in range(1,r+1):
        print(c, end="")
    for c in range(c-1,0,-1):
        print(c, end="")
    print()


'''
output - 
    1
   121
  12321
 1234321
123454321
'''