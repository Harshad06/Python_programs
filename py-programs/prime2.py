
def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def primeGenerator(n):
    num = 2
    while n:
        if isPrime(num):
            yield num
            n-=1
        num+=1
    return

iter = primeGenerator(20)
for e in iter:
    print(e, end=" ")