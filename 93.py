from itertools import combinations, product,permutations
from operator import add, sub, mul, truediv as div

ops = (add,sub,mul,div)


"""
(2*(3-4))*5 = -10 
2*((3-4)*5) = -10 
"""
def get_targets(digits,ops):
    simple = ops[0](digits[0],digits[1])
    if len(digits) == 2:
        assert(len(ops) == 1)
        return [simple]
    assert len(digits) > 2
    out = []
    for rhs in get_targets(digits[1:],ops[1:]):
        try:
            out.append(ops[0](digits[0],rhs))
        except ZeroDivisionError:
            pass
    for lhs in get_targets(digits[:-1],ops[:-1]):
        try:
            out.append(ops[-1](lhs,digits[-1]))
        except ZeroDivisionError:
            pass
    try:
        out.extend(get_targets([simple,*digits[2:]],ops[1:]))
    except ZeroDivisionError:
        pass
    return out
    

for digits in combinations(range(1,10),4):
    pass

for digits in ((1,2,3,4),):
    targets = set()
    for digorder in permutations(digits,4):
        for oporder in product(ops,repeat=3):
            targets.update(filter(lambda x: x%1 ==0 and x > 0, get_targets(digorder,oporder)))
    print(len(targets), sorted(targets))

print(get_targets((2,3,4,5),(mul,sub,mul)))