from math import log10
with open("p099_base_exp.txt") as f:
    nums = [[int(x) for x in row.split(",")] for row in f.read().split("\n")]

max = 0
max_line = -1
for i, num in enumerate(nums, 1):
    digits = 1+num[1]*log10(num[0])
    if digits > max:
        max = digits
        max_line = i

print(max_line)