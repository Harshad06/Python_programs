
def listsum(lst):
    
    total = 0
    
    for i in range(len(lst)):
        if type(lst[i]) == list:
            listsum(lst[i])
        else:
            total += lst[i]
    
    return total


lst = [[4,5],[7,8,[20]],100] 
print(listsum(lst))