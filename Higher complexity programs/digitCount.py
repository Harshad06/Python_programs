'''
count number of integers-
1000 ---->  4 digits
400 --->- 3 digits
'''

num = 1000
count=0

while num!=0:
    num //= 10
    count += 1

print("No. of digits: "+ str(count))        # str concatenation
print("No. of digits:", count)             # No need here for any concatenation



"""
num = 123456
print(len(str(num)))
"""