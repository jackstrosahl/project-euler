from math import ceil, sqrt

max_perim = 1e9

def get_area(ab,c):
    return .5*c*sqrt(ab**2-(c/2)**2)
def is_valid(ab,c):
    return ab*2 > c

total = 0

for ab in range(2,ceil(max_perim/3)):
    if ab % 10e6 == 0:
        print(f"Still going.  A=B={ab}")
    for c in (ab-1,ab+1):
        perim = ab*2 + c
        if perim > max_perim:
           continue
        area = get_area(ab,c)
        if area == int(area):
            total += perim

print(total)