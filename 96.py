grids = []
with open("p096_sudoku.txt") as f:
    lines = f.read().split("\n")
    for i in range(0,len(lines),10):
        grid = [[int(x) for x in row] for row in lines[i+1:i+10]]
        grids.append(grid)

for gridi, grid in enumerate(grids):
    def get_grid(x,y):
        return grid[y][x]
    def set_grid(x,y,val):
        grid[y][x] = val
    w = len(grid[0])
    h = len(grid)
    while True:
        solved = 0
        done = 0
        unused_counts = []
        for x in range(w):
            for y in range(h):
                if get_grid(x,y) != 0:
                    done += 1
                    continue
                used = set()
                for ox in range(w):
                    used.add(get_grid(ox,y))
                for oy in range(h):
                    used.add(get_grid(x,oy))
                chunkx = x-x%3
                chunky = y-y%3
                for ox in range(chunkx,chunkx+3):
                    for oy in range(chunky,chunky+3):
                        used.add(get_grid(ox,oy))
                unused = []
                for num in range(1,10):
                    if num not in used:
                        unused.append(num)
                if len(unused) == 1:
                    set_grid(x,y,unused[0])
                    solved += 1
                else:
                    unused_counts.append(len(unused))
        if solved == 0:
            if done < w*h:
                num = 1
                for unused in unused_counts:
                    num*=unused
                print(f"Failed Grid {gridi+1}.  Combinations: {num}")
            break