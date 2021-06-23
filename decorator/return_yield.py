
# Difference between Return and Yield in Python -

def funA():
    for i in range(5):
        return i

print(funA(), end="\n")       # 0
# > When value gets returned by a return keyword, so along with "value" the "control" also gets returned and the function ends.


#--------------------------------------------


def funB():
    for i in range(5):
        yield i

print(list(funB()))                 # [0, 1, 2, 3, 4]
# <generator object func at 0x033F7530> ----> we have to type cast it into a list/any-other-Data Structure for result.

# > When value gets returned by a yield keyword, "value" gets returned but the function does not ends, it gets paused and resumes 
#   from the same point.


