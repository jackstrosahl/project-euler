longest = 0
answer = -1
for i in range(1,int(1e6)):
    num = i
    size = 1
    while num > 1:
        size += 1
        if num%2==0:
            num /= 2
        else:
            num = num*3+1
    if size > longest:
        longest = size
        answer = i

print(answer)