from math import sqrt, floor

for i in range(1,int(1e6+1)):
    num = i
    while True:
        div_sum = 0
        for div in range(1,floor(sqrt(num))+1):
            if num % div == 0:
                div_sum += div
                if div != 1:
                    div_sum += num/div
        if num == div_sum:
            break
        num = div_sum
        if div_sum == i:
            break