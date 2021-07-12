'''
def outer(func):
    def inner(x,y):
        if x>y:
            x = 2*x
        return func(x,y)
    return inner

@outer
def add(x,y):
    return x+y


print(add(10,5))
'''


'''
s1 = 'dog'
s2 = 'god'

def anagram(s):
    return s == s[::-1]

'''


l = [9,7,2,5,3,8]

length = len(l)

for i in range(length-1):
    if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]