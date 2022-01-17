from math import sqrt

primes = set()
def is_prime(num):
    if num in primes:
        return True
    for div in range(2,int(sqrt(abs(num)))+1):
        if num % div == 0:
            return False
    primes.add(num)
    return True

best_n = 0
best_prod = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while is_prime(n**2+a*n+b):
            n += 1
        n -= 1
        if n > best_n:
            best_n = n
            best_prod = a*b

print(best_prod)
