
def A():
    print('ABC')

def A(a,b):
    print('XYZ')

# A()
A(3,4)      # XYZ

# Here, latest defined method A(a,b) will override the earlier method A().