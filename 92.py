ans = 0
shortcuts = set()
for i in range(1,int(1e7)):
    cur = i
    visited = set()
    shortcut = False
    while cur not in visited:
        if cur in shortcuts:
            shortcut = True
        visited.add(cur)
        cur = sum(int(x)**2 for x in str(cur))
    if 89 in visited or shortcut:
        ans += 1
        shortcuts.update(visited)

print(ans)