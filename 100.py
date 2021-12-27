from math import ceil, sqrt, floor
from fractions import Fraction
half = Fraction(1,2)
min_total = 1e12+1
blue_amt = sqrt(.5)

for total in range(int(min_total), int(1e13)):
    min_blue = ceil(total*blue_amt)
    done=False
    for blue in range(min_blue, min_blue+10):
        chance = Fraction(blue,total)*Fraction(blue-1,total-1)
        if chance == half:
            print(f"Blue: {blue}, Red: {total-blue}, Total: {total}, Chance: {chance}")
            done=True
            break
    if total % 1000000 == 0:
        print(f"Still going, Total: {total}")
    if done:
        break