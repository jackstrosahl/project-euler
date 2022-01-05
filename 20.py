from functools import reduce
print(sum(int(x) for x in str(reduce(lambda x1,x2:x1*x2,range(1,101)))))