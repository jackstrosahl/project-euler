# This brute force approach takes 1.5 hours.
# There is a pattern to find to make this run in reasonable time.

from math import ceil, sqrt, floor
from fractions import Fraction
half = Fraction(1,2)
min_total = 1e12+1
blue_amt = sqrt(.5)

for total in range(int(min_total),int(1e13)):
    blue = ceil(total*blue_amt)
    if total % 1e6 == 0:
        print(f"Still going, Total: {total}")
    if (blue/total)*((blue-1)/(total-1)) != .5:
        continue
    chance = Fraction(blue,total)*Fraction(blue-1,total-1)
    if chance == half:
        print(f"Blue: {blue}, Red: {total-blue}, Total: {total}, Chance: {chance}")
        break