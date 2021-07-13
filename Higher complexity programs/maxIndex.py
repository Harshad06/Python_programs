
# To find Max Index:-

lst = [10,72,54,25,90,40,120,100]

max = lst[0]
index = 0

for i in range(len(lst)):
    if lst[i] > lst[i-1]:
        max = lst[i]
        index = i
print(f'Max value is:', max)
print(f'Max value index is:', index)

'''
output:

Max value is: 120
Max value index is: 6
'''