
# sum 10 for adjacent 2 numbers??

x = [3, 2, 4, 6, 5, 9, 1, 12, 10]

for i in range(len(x)-1):
    if x[i] + x[i+1] == 10:
        print(f'Numbers are: {x[i]} & {x[i+1]}')



'''   
output:-        
# Numbers are: 4 & 6
# Numbers are: 9 & 1

-------------------------------

error if :-
if x[i] + x[i+1] == 10:
IndexError: list index out of range
it will take last element + 1, so it will OutOfIndex Error.
'''



