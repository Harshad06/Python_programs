
# Swap First and Last element in a given list.

def swap(lst):
    n=len(lst)
    lst[0], lst[n-1]= lst[n-1], lst[0]
    return print(lst)

# Driver code
lst = [10,20,30,40,50]
swap(lst)             # [50, 20, 30, 40, 10]