from math import sqrt, floor

longest = 0
answer = -1

for i in range(1,int(1e6+1)):
    num = i
    valid = True
    visited = set()
    while True:
        div_sum = 0
        visited.add(num)
        for div in range(1,floor(sqrt(num))+1):
            if num % div == 0:
                div_sum += div
                if div != 1:
                    div_sum += num/div
        if div_sum == num:
            valid = False
            break
        num = div_sum
        if num > 1e6:
            valid = False
            break
        if num == i:
            break
        elif num in visited:
            valid = False
            break
    if valid:
        if len(visited) > longest:
            longest = len(visited)
            answer = min(visited)

print(answer)