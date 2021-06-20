
# Reverse a lits along with each element in that list. 

lst = ['123', '456', '789']

rev_char = [x[::-1] for x in lst]
print(rev_char)               # ['321', '654', '987']

length = len(rev_char)

for i in range(length):
    print(rev_char[length-i-1], end=" ")            # 987 654 321 




# for list of strings -
'''
lst = ["Apple", "Banana", "Orange"]

rev_char = [x[::-1] for x in lst]
print(rev_char)

length = len(rev_char)

for i in range(length):
    print(rev_char[length-i-1], end=" ")
    

# print(lst[::-1])
'''