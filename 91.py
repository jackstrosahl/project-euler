from itertools import product, combinations
from math import acos, pi, sqrt
from decimal import Decimal
coords = filter(lambda x: x != (0,0), product(range(51),repeat=2))
tris = combinations(coords, 2)
origin = (0,0)
ans = 0
for tri in tris:
    straights = 0
    asum = 0
    a,b,c = (Decimal((edge[0][0]-edge[1][0])**2 + (edge[0][1]-edge[1][1])**2).sqrt() for edge in combinations((origin, *tri),2))
    angles = (acos((a**2+b**2-c**2)/(2*a*b)),acos((c**2+b**2-a**2)/(2*c*b)),acos((a**2+c**2-b**2)/(2*a*c)))
    if pi/2 in angles:
        ans += 1

print(ans)