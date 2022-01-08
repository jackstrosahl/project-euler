from math import factorial, floor
num_digits = 10
digits = [x for x in range(num_digits)]
answer = [x for x in digits]
perms_left = 999999

used_digits = set()
for i in range(num_digits):
    perms_per_digit = factorial(num_digits-i-1)
    target_digit_i = floor(perms_left/perms_per_digit)
    perms_left -= perms_per_digit*target_digit_i
    cur_digit_i = 0
    for j in range(num_digits):
        if j in used_digits:
            continue
        if cur_digit_i == target_digit_i:
            target_digit = j
            break
        cur_digit_i += 1
    
    used_digits.add(target_digit)
    answer[i] = target_digit

print(''.join(str(x) for x in answer))