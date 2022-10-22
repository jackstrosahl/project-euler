from collections import OrderedDict

with open('p089_roman.txt') as f:
    romans = f.read().split("\n")


roman_values = OrderedDict((
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
))

def generate_roman(num: int) -> str:
    out = ""
    while num > 0:
        for roman, value in roman_values.items():
            if num >= value:
                out += roman
                num -= value
                break
    return out

def roman_value(s: str) -> int:
    out = 0
    i = 0
    while i < len(s):
        cur = roman_values[s[i]]
        if i < len(s)-1:
            nxt = roman_values[s[i+1]]
            if nxt > cur:
                out += nxt - cur
                i += 2
                continue
        out += cur
        i += 1
    return out

ans = 0
for roman in romans:
    ans += len(roman) - len(generate_roman(roman_value(roman)))

print(ans)