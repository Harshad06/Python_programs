
# Walrus Operator allows us to accomplish 2 tasks at once -
# Assigning a value to a variable and returning that value as well.

# Syntax ---->    [name := expr]
# Here 'expr' is evaluated and assigned to the variable name and that value will also be returned.

print(num:=15)

#-----------------------

def cube(num):
    return num**3

num_list = [1,2,3,4,5]
    
l1 = [cube(x) for x in num_list if cube(x) < 20] 
print(l1)

# but here cube(x) is used twice
# hence to use it once --- use walrus operator

print([y for x in num_list if ( y:=cube(x) ) < 130 ])

#----------------------

