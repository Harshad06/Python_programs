
def even_nos(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1

it = even_nos(10)
even_list = []      # Empty list
while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break

print(even_list)



'''
> A generator-function is defined like a normal function, but whenever it needs to generate a value, 
    it does so with the yield keyword rather than return. 

> If the body of a def contains yield, the function automatically becomes a generator function.

> Generator functions return a generator object. 

> Generator objects are used either by calling the next method on the generator object or 
    using the generator object in a “for-in” loop. 
'''

'''
Difference between "return" and "yield" keyword :-
> When value gets returned by a return keyword, so along with "value" the "control" also gets returned and the function ends.
> When value gets returned by a yield keyword, "value" gets returned but the function does not ends, it gets paused and resumes 
  from the same point.

'''