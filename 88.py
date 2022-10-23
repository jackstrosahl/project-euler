from collections import Counter
from functools import lru_cache, reduce
from multiprocessing import Pool

class HCounter(Counter):
    def __key(self):
        return tuple((k,self[k]) for k in sorted(self))
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self, other):
        return self.__key() == other.__key()

@lru_cache(maxsize=int(1e4))
def get_ps_set(nums):
    cur_sum = counter_sum(nums)
    cur_prod = counter_product(nums)
    if cur_sum == cur_prod:
        return nums
    else:
        assert cur_prod < cur_sum, nums
        for val in sorted(nums):
            new_nums = HCounter(nums)
            new_nums[val] -= 1
            new_nums[val+1] += 1
            if counter_product(new_nums) <= counter_sum(new_nums):
                res = get_ps_set(new_nums)
                if res:
                    return res
        return None

def counter_product(nums):
    return reduce(lambda a,b:a*b, (num**count for num, count in nums.items()))

def counter_sum(nums):
    return sum(num*count for num, count in nums.items())

def get_psn(k):
    if k % 100 == 0:
        print(f"Still going, k={k}")
    nums = get_ps_set(HCounter({1:k}))
    return counter_sum(nums)

with Pool() as pool:
    res = pool.map(get_psn, range(2,12001),chunksize=100)

print(sum(set(res)))