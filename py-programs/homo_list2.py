
# check if list is homogeneous or not?

def checkList(lst):
    
    ele = lst[0]
    chk = True

    # print(type(ele))

    # Comparing each element with first item
    for item in lst:
        if type(item) != type(ele):
            print(item)
            chk = False
            break
    
    if (chk==True):
        print("List contains items of same data type")
    else:
        print("List is not Homogenous")


# Driver Code
l1 = [10,20,30,"abc", True, 50]
checkList(l1)

l2 = [10,20,30,40,50]
checkList(l2)