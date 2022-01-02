from math import ceil, sqrt
from decimal import Decimal

max_perim = 1e9

def get_area(a,b,c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))
def is_valid(a,b,c):
    return not (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a))

total = 0

for ab in range(2,ceil(max_perim/3)):
    if ab % 10e6 == 0:
        print(f"Still going.  A=B={ab}")
    for c in (ab-1,ab+1):
        perim = ab+ab + c
        if perim > max_perim:
           continue
        area = get_area(Decimal(ab),Decimal(ab),Decimal(c))
        if area.is_integer():
            total += perim

print(total)