"""
import re

sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.group())



class A:
  __salary=5000
  def total(self, increment):
      self._salary+=increment

obj=A()
obj.total(100)
print(obj.__salary)




x = 'abcd'
for i in range(len(x)):
      x[i].upper()
print(x)




def f(x = 100, y = 100):
     return(x+y, x-y)
x, y = f(y = 200, x = 100)
print(x, y)




lst = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lst)-1, -1, -1):
      print( lst[i] , end = ' ')





print(bin((2**16)-1))
print('{}'.format(bin((2**16)-1)))




a=[3,4,9,0,1,12,5]
b=a.sort()
print(b)




dict1={"a":10,"b":2,"c":3}
str1=""
for i in dict1:
  str1=str1+str(dict1[i])+" "
  str2=str1[:-1]
print(str2[::-1])




x=12
def f1(a,b=x):
  print(a,b)
x=15
f1(4)




def my_func(num):
    data = [0]
    for i in range(1, num+1):
        data.append(data[i >> 1] + int(i & 1))
        return data
num = 6
print(my_func(num))





list1 = []
list2 = []
if list1 is list2:
    pass

"""

def my_func(nums):
    count = 0
    for i, j in enumerate(nums):
        if i > count:
            return False
        count = max(count, i + j)
    return True

if __name__ == "__main__":
    print(my_func([3, 2, 1, 0, 4]))

