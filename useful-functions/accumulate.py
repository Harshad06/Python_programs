
"""
        accumulate() function
> accumulate() in “itertools” module
> accumulate() returns a iterator containing the intermediate results. 
> The last number of the iterator returned is summation value of the list.

"""
import itertools
import operator

n = [1,2,3,5,10,20]
print(list(itertools.accumulate(n, operator.add)))