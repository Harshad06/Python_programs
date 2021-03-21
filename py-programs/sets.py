# SETS in Python
# Denoted by {} curly brackets

'''
num = [1,1,2,2,3,3,4,4,5,5]
uniques = set(num) 
print(uniques)          #output: {1, 2, 3, 4, 5}

second = {6,7,7,6}
print(second)           #output: It will only show unique values : {6, 7}

second.add(100)
print(second)
print(len(second))

second.remove(100)
print(second)
'''

first = {1,2,3,4}
second = {1,5}

# Union of sets-
print(first | second)       # o/p : {1, 2, 3, 4, 5}

# Intersection in sets-
print(first & second)       # o/p : {1}

# Difference in sets-
print(first - second)       # o/p : {2, 3, 4} - first set has these additional numbers which set 2 doesn't.

# Caret in sets:-
print(first ^ second)      # o/p : {2,3,4,5} - elements in both sets but not common ones



if 2 in first:
    print("yes")            # o/p : yes