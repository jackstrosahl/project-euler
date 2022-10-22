from itertools import combinations, combinations_with_replacement,permutations
from operator import add, sub, mul, truediv as div

ops = (add,sub,mul,div)

def get_targets(digits,ops,lhs=None):
    # print(digits,ops,lhs)
    if len(digits) == 0:
        return [lhs]
    rhs = digits[0]
    digits = digits[1:]
    if lhs==None:
        return get_targets(digits,ops,rhs)
    op = ops[0]
    ops = ops[1:]
    out = []
    for orhs in get_targets(digits,ops,rhs):
        try:
            out.append(op(lhs,orhs))
        except ZeroDivisionError:
            pass
    if len(ops) > 0: 
        try:
            out.extend(get_targets(digits,ops,op(lhs,rhs)))
        except ZeroDivisionError:
            pass
    return out
    

for digits in combinations(range(1,10),4):
    pass

for digits in ((1,2,3,4),):
    targets = set()
    for digorder in permutations(digits,4):
        for oporder in combinations_with_replacement(ops,3):
            targets.update(filter(lambda x: x % 1 == 0 and x > 0, get_targets(digorder,oporder)))
    print(len(targets), sorted(targets))

print(get_targets((1,2,3,4),(add,mul,sub)))