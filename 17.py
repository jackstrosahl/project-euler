from num2words import num2words
from re import sub
print(sum(len(sub(" |-", "",num2words(i))) for i in range(1,1001)))