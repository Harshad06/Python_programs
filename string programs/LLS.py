
# list in a list of strings - 

test_list = [["J", "o", "y"], ["i", "s"], ["t","h","e"], ["b", "e", "s", "t"]]

new_list = [''.join(x) for x in test_list]          # ['Joy', 'is', 'best']

print(' '.join(new_list))           # Joy is best



# Alternatively
# print(' '.join([''.join(x) for x in test_list]))
