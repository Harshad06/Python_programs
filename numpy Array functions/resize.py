
import numpy as np

a = np.array([0,1,2,3,4])
print(a)
print(a.shape)

print("------------")

# If we use "np.resize" --> It will give us new array, but won't change the original array.
print(np.resize(a, (2,3)))
print(a)
print(a.shape)


print("------------")

# If we use "a.resize" --> It will change the original array and will resize it.
a.resize((5,2))
print(a)
print(a.shape)