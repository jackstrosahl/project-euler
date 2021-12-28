num = 20
while True:
    good = True
    for div in range(2,20):
        if num % div != 0:
            good = False
            break
    if good:
        print(num)
        break
    num += 20