
# sum 10 for adjacent 2 numbers??
'''
x = [3, 2, 4, 6, 5, 9, 1, 12, 10]

for i in range(len(x)-1):
    if x[i] + x[i+1] == 10:
        print(f'Numbers are:', x[i], '&', x[i+1])
    
output:-        
# Numbers are: 4 & 6
# Numbers are: 9 & 1
-------------------------------
error if :-
if x[i] + x[i+1] == 10:
IndexError: list index out of range
it will take last element + 1, so it will OutOfIndex Error.
'''



# sum 10 for any 2 numbers??

def indices_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target: 
                # print(i,j)      # indices will be printed
                print(nums[i],nums[j], "= 10" )     # To print elements 

# Driver code
if __name__=="__main__":
    nums = [3, 2, 4, 6, 5, 9, 8, 1, 7, 10]
    target = 10
    indices_sum(nums,target)
'''
# output -
Indices:
3 7
2 8
4 6
9 1 

Elements:-
3 7 = 10
2 8 = 10
4 6 = 10
9 1 = 10
'''