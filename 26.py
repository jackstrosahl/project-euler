from collections import Counter
from decimal import ROUND_DOWN, Decimal, getcontext
import re
prec = 5000
getcontext().prec = prec
PLACES = Decimal(10) ** -prec
pattern =r'([0-9]{1,})\1{1,}$'

best_length = 0
best_d = -1
for d in range(2,1000):
    num = (Decimal(1) / Decimal(d)).quantize(PLACES)
    val = str(num)[2:]
    match = re.search(pattern, val)
    if match is None:
        continue
    while True:
        new_match = re.search(pattern, match.group(1))
        if new_match is not None:
            match = new_match
        else:
            break
    cycle_length = len(match.group(1))
    if cycle_length > best_length:
        best_length = cycle_length
        best_d = d

print(best_d)