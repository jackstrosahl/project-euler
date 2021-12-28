breaking = False
for c in range(3,1000):
    if c * 3 < 1000:
        continue
    for b in range(2,c):
        if c + b*2 < 1000:
            continue
        for a in range(1,b):
            if a+b+c!=1000:
                continue
            if a**2+b**2==c**2:
                print(a*b*c)
                breaking = True
                break
        if breaking:
            break
    if breaking:
        break