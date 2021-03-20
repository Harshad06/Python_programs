""" 
        REDUCE Function:-
> Applies same operation to items of a sequence.
> uses result of operation as first param of next operation
> Returns an item and NOT a list

> reduce function is defined under "functools" module. Hence we need to import this module.

"""
import functools

n = [4,3,2,1]
# print(functools.reduce(lambda x,y:x*y, n))

"""
import functools
import operator

n = [4,3,2,1]
print(functools.reduce(operator.mul,n))

"""