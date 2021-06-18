'''
count number of integers-
1000 ----  4 
400 ---- 3 
'''
"""
num = 1000
count=0

while num!=0:
    num //= 10
    count += 1

print("No. of digits: "+ str(count))
"""
"""
num = 123456
print(len(str(num)))
"""

# ------------------------------------------------
'''
find count of char in string -
name = "aabbbcccdddd"
a=2
b=3
c=4 and so on
'''
'''
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('abbcccdddd'))
'''
# ------------------------------------------------


"""
import functools

arr = [1,2,3,4,5,6,7,8,9,10]

print(functools.reduce(lambda x,y:x+y, arr))
"""


"""
from typing import Counter


name = "aabbbcccdddd"

d = Counter(name)
print(d)
"""


# Python3 code to demonstrate
# each occurrence frequency using
# naive method

# initializing string
test_str = "GeeksforGeeks"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

# printing result
print ("Count of all characters in GeeksforGeeks is :\n "
										+ str(all_freq))
