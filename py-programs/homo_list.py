
# check if list is homogeneous or not?

l1 = [10,20,30,40,50,60]

print("The original list is: ", str(l1))

res = True

for element in l1:
    if not isinstance(element, type(l1[0])):
        res = False
        break

print ("Do all elements have same type : " + str(res))