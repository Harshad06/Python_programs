
# Find the Missing Number

def getMissingNo(A):
    n = len(A)
    total = (n+1)*(n+2)//2
    sum_of_A = sum(A)
    return total - sum_of_A

# Driver code
A = [1,2,3,5,6]
miss = getMissingNo(A)
print("Missing Num is:", miss)