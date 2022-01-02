triangle_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = [[int(x) for x in row.split()] for row in triangle_str.split("\n")]

def get(pos):
    x,y = pos
    return triangle[y][x]

def is_valid(pos):
    x,y = pos
    return y >= 0 and y < len(triangle) and x >= 0 and x <= y

def get_best_sum(pos=(0,0)):
    x,y = pos
    best_sum = 0
    for dx in range(2):
        next_pos = (x+dx,y+1)
        if not is_valid(next_pos):
            continue
        cur_sum = get_best_sum(next_pos)
        if cur_sum > best_sum:
            best_sum = cur_sum
    return best_sum + get(pos)

print(get_best_sum())