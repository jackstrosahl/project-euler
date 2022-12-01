from math import inf, log
from sympy import primerange

limit = 50e6
powers = (2,3,4)

max_base = limit**(1/min(powers))

primes = tuple(primerange(0,max_base+1))

prime_indices = list(0 for _ in powers)

def get_value():
    return sum(primes[prime_i] ** power for prime_i, power in zip(prime_indices, powers))

ans = 0
values = []
indices_valid = True
while indices_valid:
    value = get_value()
    values.append(value)
    ans += 1

    indices_valid = False
    for i in range(len(powers)):
        prime_indices[i] += 1
        new_val = inf
        if prime_indices[i] < len(primes):
            new_val = get_value()

        if new_val < limit:
            indices_valid = True
            break
        elif i < len(powers) - 1:
            prime_indices[i] = 0


print(ans)
