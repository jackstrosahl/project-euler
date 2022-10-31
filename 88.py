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
    f_score = defaultdict(lambda: inf)
    prev = defaultdict(lambda: None)

    def adjacent_nums(nums):
        for val in sorted(nums):
            assert nums[val] >= 0
            new_nums = HCounter(nums)
            new_nums[val] -= 1
            if new_nums[val] == 0:
                del new_nums[val]
            new_nums[val+1] += 1
            yield new_nums

    nums = HCounter({1:k})
    q[nums] = 0
    dist[nums] = 0
    f_score[nums] = sum_prod_diff(nums)
    while len(q) > 0:
        nums = q.popitem()[0]
        # print(list(nums.elements()))
        if sum_prod_diff(nums) == 0:
            return nums
        for adjacent in adjacent_nums(nums):
            diff = abs(sum_prod_diff(adjacent))
            alt = dist[nums] + 1
            if alt < dist[adjacent]:
                dist[adjacent] = alt
                f = alt + diff
                f_score[adjacent] = f
                q[adjacent] = f
                prev[adjacent] = nums

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

with Pool() as pool:
    res = set(pool.map(get_psn, range(2,12001),chunksize=100))

# res = set(map(get_psn, range(2,13)))

print(sorted(res))

print(sum(res))