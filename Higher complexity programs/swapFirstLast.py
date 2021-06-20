
# Swap First and Last element in a given list.

def Swap(lst):
    n=len(lst)
    lst[0], lst[n-1]= lst[n-1], lst[0]
    return print(lst)

# Driver code
lst = [10,20,30,40,50]
Swap(lst)