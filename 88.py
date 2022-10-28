from collections import Counter
from functools import reduce
from multiprocessing import Pool

class HCounter(Counter):
    def __key(self):
        return tuple((k,self[k]) for k in sorted(self))
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self, other):
        return self.__key() == other.__key()

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
    s = []
    visited = set()
    nums = HCounter({1:k})
    s.append(nums)
    while len(s) > 0:
        nums = s.pop()
        if nums in visited:
            continue
        visited.add(nums)
        diff = counter_sum(nums) - counter_product(nums)
        if diff == 0:
            return nums
        elif diff < 0:
            continue
        for val in sorted(nums, reverse=True):
            assert nums[val] >= 0
            new_nums = HCounter(nums)
            new_nums[val] -= 1
            if new_nums[val] == 0:
                del new_nums[val]
            new_nums[val+1] += 1
            s.append(new_nums)

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
    res = set(map(get_psn, range(2,12001)))

print(res)

print(sum(res))