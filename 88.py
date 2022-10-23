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
def get_ps_set(nums,tsum,tprod):
    cur_sum = counter_sum(nums)
    cur_prod = counter_product(nums)
    if cur_sum == tsum and cur_prod == tprod:
        return nums

    assert cur_sum < tsum or cur_prod < tprod, (nums,tsum,tprod)

    val = min(nums)
    new_nums = HCounter(nums)
    assert new_nums[val] > 0
    new_nums[val] -= 1
    if new_nums[val] == 0:
        del new_nums[val]
    if len(new_nums) > 0 and tprod % val == 0 and counter_sum(new_nums) <= tsum and counter_product(new_nums) <= tprod:
        res = get_ps_set(new_nums,tsum-val,tprod/val)
        if res:
            res[val] += 1
            return res

    for val in sorted(nums):
        new_nums = HCounter(nums)
        new_nums[val] -= 1
        if new_nums[val] == 0:
            del new_nums[val]
        new_nums[val+1] += 1
        if counter_sum(new_nums) <= tsum and counter_product(new_nums) <= tprod:
            res = get_ps_set(new_nums,tsum,tprod)
            if res:
                return res
    
    
    
    return None

def counter_product(nums):
    return reduce(lambda a,b:a*b, (num**count for num, count in nums.items()))

def counter_sum(nums):
    return sum(num*count for num, count in nums.items())

def get_psn(k):
    print(f"Still going, k={k}")
    n = k
    nums = None
    while nums is None:
        nums = get_ps_set(HCounter({1:k}),n,n)
        n+=1
    return counter_sum(nums)

with Pool() as pool:
    res = map(get_psn, range(2,12001))

print(sum(set(res)))