from math import floor,sqrt
max_non_abundant_sum = 28123

abundant = []

for num in range(1,max_non_abundant_sum+1):
    divs = set()
    for div in range(1,floor(sqrt(num))+1):
        if num % div == 0:
            divs.add(div)
            if div != 1:
                divs.add(num/div)
    if sum(divs) > num:
        abundant.append(num)

abundant_sums = set()

for a in abundant:
    for b in abundant:
        abundant_sums.add(a+b)

print(sum(i if i not in abundant_sums else 0 for i in range(1,max_non_abundant_sum+1)))