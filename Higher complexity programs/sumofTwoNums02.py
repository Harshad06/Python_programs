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