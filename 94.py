from math import ceil
from decimal import Decimal
from multiprocessing import Pool

max_perim = 1e9

def get_area(a,b):
    return (b/4)*((4*a**2-b**2).sqrt())

def check_area(ab):
    ans = 0
    if ab % 10e6 == 0:
        print(f"Still going.  A=B={ab}")
    for c in (ab-1,ab+1):
        perim = ab+ab + c
        if perim > max_perim:
           continue
        area = get_area(Decimal(ab),Decimal(c))
        if area % 1 == 0:
            ans += perim
    return ans

with Pool() as pool:
    res = pool.map(check_area, range(2,ceil(max_perim/3)+10), chunksize=10000)

print(sum(res))