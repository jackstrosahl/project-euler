from math import sqrt
total = 0
num = 2
while True:
    prime = True
    for div in range(2,int(sqrt(num)+1)):
        if num % div == 0:
            prime = False
            break
    if prime:
        total += num
    num += 1
    if num >= 2e6:
        print(total)
        break