
# Program to replace None in the List with previous value

x  =  [2,None,3,4,None,None,10,12,None]

for i in range(len(x)):
    if x[i] == None:
        x[i] = x[i-1]

print(x)            # [2, 2, 3, 4, 4, 4, 10, 12, 12]



'''
input: [None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
output: [None, None, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
'''