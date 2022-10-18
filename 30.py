power = 5
ans = 0
for x in range(2,int(1e6)):
    power_sum = sum(int(digit)**power for digit in str(x))
    if power_sum == x:
        ans += x

print(ans)