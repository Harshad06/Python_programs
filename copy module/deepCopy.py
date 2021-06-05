
# A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list.append([4,4,4])

old_list[1][1] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)


# print("Old list:", id(old_list))
# print("New list:", id(new_list))