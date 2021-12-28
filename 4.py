palindromes = []
for i in range(100,1000):
    for j in range(100,1000):
        val = i*j
        s = str(val)
        if s == s[::-1]:
            palindromes.append(val)

print(max(palindromes))