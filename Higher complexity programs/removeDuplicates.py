
# Python code to remove duplicate elements

"""
Input : [2, 4, 10, 20, 5, 2, 20, 4]
Output : [2, 4, 10, 20, 5]

Input : [28, 42, 28, 16, 90, 42, 42, 28]
Output : [28, 42, 16, 90]
"""


def Remove(duplicate):
    final_lst = []
    for num in duplicate:
        if num not in final_lst:
            final_lst.append(num)
    return final_lst

# Driver code
dup = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(dup))               # [2, 4, 10, 20, 5]



"""
# Using SET -

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))

"""