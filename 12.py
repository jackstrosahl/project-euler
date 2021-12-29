from math import sqrt, ceil

i = 1
num = 0
while True:
    num += i
    i += 1
    divs = 0
    for div in range(1,ceil(sqrt(num))):
        if num % div == 0:
            divs += 2
    if divs > 500:
        print(num)
        break