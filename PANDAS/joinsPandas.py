## MERGE Function
# JOINS in PANDAS ----> [inner/outer/right/left/index]

# importing pandas
import pandas as pd

# Creating Dictionary 1
data1 = {'id': [1, 2, 10, 12],
	    'val1': ['a', 'b', 'c', 'd']}

a = pd.DataFrame(data1)
# print(a)


# Creating Dictionary 2
data2 = {'id': [1, 2, 9, 8],
	    'val2': ['p', 'q', 'r', 's']}

b = pd.DataFrame(data2)
# print(b)


# inner join
df = pd.merge(a, b, on='id', how='inner')
print("Inner Join: \n", df, end="\n")

# outer join
df = pd.merge(a, b, on='id', how='outer')
print("Outer Join: \n", df, end="\n")

# left join
df = pd.merge(a, b, on='id', how='left')
print("Left Join: \n", df, end="\n")

# right join
df = pd.merge(a, b, on='id', how='right')
print("Right Join: \n", df, end="\n")