
# Reverse list without using any built-in method.

lst = [1,2,3,4,5,6,7,8,90,100]
length = len(lst)

for i in range(length):
    print(lst[length-i-1], end=" ")         # 100 90 8 7 6 5 4 3 2 1




"""
lst = ["Apple", "Banana", "Orange", "Kiwi", "Strawberry", "Mango"]

length = len(lst)

for i in range(length):
    print(lst[length-i-1], end=" ")

"""