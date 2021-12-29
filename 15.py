w = 20
h = 20
def count_solutions(pos=(0,0)):
    print(pos)
    num_solutions = 0
    x,y = pos
    if x+1 <= w:
        num_solutions += count_solutions((x+1,y))
    if y+1 <= h:
        num_solutions += count_solutions((x,y+1))
    if x == w and y == h:
        num_solutions += 1
    return num_solutions

print(count_solutions())