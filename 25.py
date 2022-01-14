last = (1,1)
i = 2
while True:
    i += 1
    val = sum(last)
    if len(str(val)) >= 1000:
        break
    last = (last[1],val)

print(i)