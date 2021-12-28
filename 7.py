from math import sqrt
num_primes = 0
num = 2
while True:
    prime = True
    for div in range(2,int(sqrt(num)+1)):
        if num % div == 0:
            prime = False
            break
    if prime:
        num_primes += 1
    if num_primes == 10001:
        print(num)
        break
    num += 1