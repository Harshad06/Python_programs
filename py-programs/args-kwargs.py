
# args/kwargs allows python functions to accept
# arbitary/unspecified amt of arguments & keyword arguments

# Arguments
def print_args(*args):
    print(f"These are my arguments : {args}")

print_args([1,2,3],(20,30),{'key': 4})

#---------------------------------------------------

# Keyword Arguments
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

print_kwargs(x="Hello", y="world")