
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

print(old_list is new_list)


"""
In Python, Assignment statements do not copy objects, they create bindings between a target and an object. 

When we use = operator user thinks that this creates a new object; well, it doesn’t. 

It only creates a new variable that shares the reference of the original object.
"""