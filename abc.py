
lst = ["Apple", "Banana", "Orange"]

rev_char = [x[::-1] for x in lst]
print(rev_char)

length = len(rev_char)

for i in range(length):
    print(rev_char[length-i-1], end=" ")
    

# print(lst[::-1])

