
def is_prime(n):
    for i in range(2,n):
        if not (n % i):
            return False
    return True

for n in range(1,20):
    if is_prime(n):
        print(n)
        #print(n, end=" ")      # Print integers in one line only


