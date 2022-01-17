size = 1001
answer = 1
cur_num = 1

for s in range(3,size+1,2):
    for i in range(4):
        cur_num += s-1
        answer += cur_num

print(answer)