
# Python program to print duplicates from a list of integers

"""
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
"""

from collections import Counter


l1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

d = Counter(l1)             
print(d)                    # Counter({20: 3, -20: 3, 30: 2, 60: 2, 10: 1, 40: 1, 50: 1})

new_list = [ item for item in d if d[item]>1 ]
print(new_list)             # [20, 30, -20, 60]