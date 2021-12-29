grids = []
with open("p096_sudoku.txt") as f:
    lines = f.read().split("\n")
    for i in range(0,len(lines),10):
        grid = [[int(x) for x in row] for row in lines[i+1:i+10]]
        grids.append(grid)

answer = 0

for gridi, grid in enumerate(grids):
    def get_grid(x,y):
        return grid[y][x]
    def set_grid(x,y,val):
        grid[y][x] = val
    w = len(grid[0])
    h = len(grid)
    zeros = []
    for x in range(w):
        for y in range(h):
            if get_grid(x,y) == 0:
                zeros.append((x,y))
    zerosi = 0
    while zerosi < len(zeros):
        x,y = zeros[zerosi]
        val = get_grid(x,y)
        if val == 9:
            zerosi -= 1
            set_grid(x,y,0)
            continue
        val += 1
        set_grid(x,y,val)

        checks = []
        for ox in range(w):
            checks.append((ox,y))
        for oy in range(h):
            checks.append((x,oy))
        chunkx = x-x%3
        chunky = y-y%3
        for ox in range(chunkx,chunkx+3):
            for oy in range(chunky,chunky+3):
                checks.append((ox,oy))

        valid = True
        for checkx,checky in checks:
            if checkx == x and checky == y:
                continue
            if get_grid(checkx,checky) == val:
                valid = False
                break
        if valid:
            zerosi += 1
    answer += int(''.join(str(x) for x in grid[0][0:3]))

print(answer)