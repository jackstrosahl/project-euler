from math import sqrt,floor

num = 600851475143
factors = set()
for div in range(2,int(sqrt(num))):
    if num % div == 0:
        factors.add(div)
        factors.add(num/div)

primes = []
for factor in factors:
    prime = True
    for div in range(2,int(sqrt(factor))):
        if factor % div == 0:
            prime = False
            break
    if prime:
        primes.append(factor)

print(max(primes))