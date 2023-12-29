# %%
txt = open('input.txt').read().splitlines()
m, n = len(txt), len(txt[0])

# %%
def travel(position, direction, visited):
    x, y = position
    dx, dy = direction
    while True:
        if not (0 <= x < m and 0 <= y < n):
            return visited
        
        if (x, y) in visited:
            if (dx, dy) in visited[(x, y)]:
                return visited
        else:
            visited[(x, y)] = list()
        visited[(x, y)] += [(dx, dy)]

        if txt[x][y] == '\\':
            (dx, dy) = (dy, dx)
        if txt[x][y] == '/':
            (dx, dy) = (-dy, -dx)
        if txt[x][y] == '-':
            if dy == 0:
                travel((x, y + 1), (0, 1), visited)
                travel((x, y - 1), (0, -1), visited)
                return visited
        if txt[x][y] == '|':
            if dx == 0:
                travel((x + 1, y), (1, 0), visited)
                travel((x - 1, y), (-1, 0), visited)
                return visited
        x += dx
        y += dy

# %%
p1 = len(travel((0, 0), (0, 1), {}))
print(f'p1 = {p1}')

# %%
best_start = (0, 0), (0, 1)
best_energized = len(travel(*best_start, {}))

def compare(position, direction):
    global best_start, best_energized
    energized = len(travel(position, direction, {}))
    if energized > best_energized:
        best_start = position, direction
        best_energized = energized

for x in range(m):
    compare((x, 0), (0, 1))
    compare((x, n - 1), (0, -1))

for y in range(n):
    compare((0, y), (1, 0))
    compare((m - 1, y), (-1, 0))

print(f'p2 = {best_energized}')
