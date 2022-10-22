from collections import defaultdict
from itertools import combinations_with_replacement, combinations
squares = []
i = 1
while i**2 < 100:
    squares.append(i**2)
    i+=1

mutex_digits = defaultdict(lambda: set())

def add_excl(a,b):
    mutex_digits[a].add(b)
    # mutex_digits[b].add(a)
    
for square in squares:
    if square < 10:
        add_excl(0,square)
    else:
        add_excl(*(int(x) for x in str(square)))

def check_cubes(a,b):
    for digit, others in mutex_digits.items():
        for other in others:
            if digit in a and other in b or digit in b and other in a:
                continue
            return False
    return True

def add_flips(a):
    if 6 in a:
        a.add(9)
    elif 9 in a:
        a.add(6)

ans = 0
for cube_a, cube_b in combinations_with_replacement(combinations(range(10),6),2):
    cube_a = set(cube_a)
    cube_b = set(cube_b)
    add_flips(cube_a)
    add_flips(cube_b)
    if check_cubes(cube_a,cube_b):
        ans += 1

print(ans)
