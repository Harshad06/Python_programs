
my_list = ["Apple", "Banana", "Orange", "Kiwi"]


for x in my_list[::-1]:
    print(x)
    print(list(x))


for y in reversed(my_list):
    print(y)


""" 
# reversed v/s .reverse() function
# .reverse() function --> This will the change the original list itself

a = my_list.reverse()
print(my_list)

"""