
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if not (n%i):
            return False
    return True

for n in range(2,20):
    if is_prime(n):
        print(n, end=" ")