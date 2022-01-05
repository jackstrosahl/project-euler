from math import sqrt, floor

answer = 0

for i in range(1,int(10001)):
    num = i
    valid = True
    for _ in range(2):
        div_sum = 0
        for div in range(1,floor(sqrt(num))+1):
            if num % div == 0:
                div_sum += div
                if div != 1:
                    div_sum += num/div
        if div_sum == num:
            valid = False
            break
        num = div_sum
    
    if valid and num == i:
        answer += i

print(answer)