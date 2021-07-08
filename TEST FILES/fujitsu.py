
# 2, 4 , 4, 12 
# replace value of None by its current front number
lst  =  [2,None,3,4,None,None,10,12,None]

x  =  [2,None,3,4,None,None,10,12,None]

for i in range(len(x)):
    if x[i] == None:
        x[i] = x[i-1]

print(x)

'''
move all zeroes to the end:-

lst  =  [1,7,0,0,10,12,0,5,6]

l1 = [x for x in lst if x!=0]
l2 = [x for x in lst if x==0]

print(l1+l2)       # [1, 7, 10, 12, 5, 6, 0, 0, 0]
'''

'''
from typing import Counter

lst  =  ['one', 'two','three','one', 'two','three', 'one', 'four']

d = Counter(lst)
print(d)
'''