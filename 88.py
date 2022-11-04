from collections import Counter, defaultdict
from math import inf
from functools import reduce
from multiprocessing import Pool
from heapdict import heapdict

class HCounter(Counter):
    def __key(self):
        return tuple((k,self[k]) for k in sorted(self))
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self, other):
        return self.__key() == other.__key()


def sum_prod_diff(nums):
    return counter_sum(nums) - counter_product(nums)

"""
111
    112
        122
            123
            222
        113
            123
            114
"""
def get_ps_set(k):
    q = heapdict()
    dist = defaultdict(lambda: inf)

    nums = HCounter({1:k})
    q[nums] = 0
    dist[nums] = 0
    while len(q) > 0:
        nums = q.popitem()[0]
        # print(list(nums.elements()))
        nums_prod = counter_product(nums)
        nums_sum = counter_sum(nums)
        if nums_sum - nums_prod == 0:
            return nums
        for val in sorted(nums):
            adjacent = HCounter(nums)
            adjacent[val] -= 1
            if adjacent[val] == 0:
                del adjacent[val]
            adjacent[val+1] += 1
            alt = dist[nums] + ((nums_prod/val)*(val+1)) - nums_prod
            if alt < dist[adjacent]:
                dist[adjacent] = alt
                q[adjacent] = alt

    return None

def counter_product(nums):
    return reduce(lambda a,b:a*b, (num**count for num, count in nums.items()))

def counter_sum(nums):
    return sum(num*count for num, count in nums.items())

def get_psn(k):
    if k % 100 == 2:
        print(f"Still going, k={k}")
    nums = get_ps_set(k)
    return counter_sum(nums)

if __name__ == "__main__":
    with Pool() as pool:
        res = set(pool.map(get_psn, range(2,12001),chunksize=100))

    # res = set(map(get_psn, range(2,100)))

    print(sorted(res))

    print(sum(res))