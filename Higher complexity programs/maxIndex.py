
# To find Max Index:-

lst = [10000,72,54,25,90,40,120,100,300]

max = lst[0]
index = 0

for i in range(1, len(lst)):      # can use only ---> "len(lst)" in place of (1, len(lst))
    if lst[i] > max:        # can also use ---> lst[i-1] in place of 'max'
        max = lst[i]
        index = i
print(f'Max value is: {max}')
print(f'Max value index is: {index}')

'''
output:

Max value is: 120
Max value index is: 6
'''