from time import time


def iter(n):
    while n > 0:
        n -= 1

def recur(n):
    if n == 0:
        return
    return recur(n-1)

n = 500
start = time()
iter(n)
print(f"Iterative: {time()-start}")
start = time()
recur(n)
print(f"Recursive: {time()-start}")
