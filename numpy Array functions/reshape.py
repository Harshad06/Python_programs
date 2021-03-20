
import numpy as np

a = np.arange(10)
print(a)
print(a.shape)

b = np.reshape(a, (5,2))
print(b.shape)


# do not use a.shape() --- parenthesis 
# use as a.shape only


# Reshape() doesn't change shape of data unlike resize()