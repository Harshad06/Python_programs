
"""
        accumulate() function
> accumulate() belongs to “itertools” module
> accumulate() returns a iterator containing the intermediate results. 
> The last number of the iterator returned is operation value of the list.

"""
import itertools
import operator

n = [1,2,3,5,10]
print(list(itertools.accumulate(n, operator.add)))

print(list(itertools.accumulate(n, operator.mul)))