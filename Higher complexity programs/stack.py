
# Python program to demonstrate stack implementation using list

stack = []

# append() function to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() fucntion to pop element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty



# for larger no. of elements in stack, use - 
'''
while stack!=0:
    print(stack.pop())
'''
