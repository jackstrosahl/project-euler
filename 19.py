
days_month = (31,28,31,30,31,30,31,31,30,31,30,31)
day_index = 0
answer = 0
for year in range(1900,2001):
    for month in days_month:
        if day_index % 7 == 6 and year != 1900:
            answer += 1
        if month == 28 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month += 1
        day_index += month

print(answer)