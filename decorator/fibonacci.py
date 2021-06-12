
# A simple generator for Fibonacci Numbers
def fibonacci(limit):
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1    

    # One by one yield next Fibonacci Number
    while(a<limit):
        yield a
        a, b = b, a+b 

# Iterating over the generator object using for-in loop.
print(f'Using for-in loop')

for i in fibonacci(5):
    print(i)

print("----------------------")

# Create a generator object
it = fibonacci(6)

# Iterating over the generator object using next.
print(f'Using next()')

fib_list = []
while True:
    try:
        fib_list.append(next(it))
    except StopIteration:
        break
 
print(fib_list)


# So a generator function that returns an generator object that is iterable, i.e., can be used as an Iterators .