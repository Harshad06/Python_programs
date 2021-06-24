
# Find the sum of all the elements of the given list below - 

import functools

lst = [1,2,3,[3,4,5],[6,7,8],[1,4,6],8,9]

new1 = [x for x in lst if type(x)==int]
# print(new1)               # [1, 2, 3, 8, 9]

new2 = [sum(x) for x in lst if (type(x)==list)]
# print(new2)               # [12, 21, 11]

newList = new1 + new2 
# print(newList)            # [1, 2, 3, 8, 9, 12, 21, 11]

n = (functools.reduce(lambda x,y:x+y, newList))
print(n)                    # 67