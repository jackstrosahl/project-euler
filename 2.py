last = (1,2)
total = sum(i if i%2==0 else 0 for i in last)
while True:
    val = sum(last)
    if val >= 4e6:
        break
    if val % 2 == 0:
        total += val
    last = (last[1], val)
    print(val)
print(total)