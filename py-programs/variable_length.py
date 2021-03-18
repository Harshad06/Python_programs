
# variable length argument in python

def average(*t):
    avg = sum(t)/len(t)
    print("Average is : ", avg)

average(1,2,3)
average(20,30,40,50)
average(11,22,33,44,55,66,77,88,99)


