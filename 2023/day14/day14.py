# %%
from itertools import batched

txt = open('input.txt').read().splitlines()

def to_str(lines):
    return ''.join([''.join(line) for line in lines])

def tilt(rocks, direction):
    changed = True
    offset_i, offset_j = {
        'north': (-1, 0),
        'south': (1, 0),
        'east': (0, 1),
        'west': (0, -1),
    }.get(direction)

    while changed:
        changed = False
        for i in range(len(rocks)):
            if i + offset_i not in range(len(rocks)):
                continue
            for j in range(len(rocks[i])):
                if j + offset_j not in range(len(rocks[i])):
                    continue
                if rocks[i][j] == 'O' and rocks[i + offset_i][j + offset_j] == '.':
                    rocks[i][j] = '.'
                    rocks[i + offset_i][j + offset_j] = 'O'
                    changed = True
    return rocks

def tilt_cycle(rocks):
    for direction in ['north', 'west', 'south', 'east']:
        rocks = tilt(rocks, direction)
    return rocks

def total_load(rocks):
    load = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            if rocks[i][j] == 'O':
                load += len(rocks) - i
    return load

# %%
rocks = [list(line) for line in txt]
p1 = total_load(tilt(rocks, 'north'))
print(f'p1 = {p1}')

# %%
rocks = [list(line) for line in txt]
n = 0

history = dict()
history[to_str(rocks)] = n

while n < 1e9:
    n += 1
    rocks = tilt_cycle(rocks)

    if to_str(rocks) in history:
        break
    else:
        history[to_str(rocks)] = n

start = history[to_str(rocks)]
cycle = n - start
offset = start + (1e9 - start) - (1e9 - start) // cycle * cycle

rocks_str = next(k for k, v in history.items() if v == offset)
rocks = list(batched(rocks_str, len(txt[0])))

p2 = total_load(rocks)
print(f'p2 = {p2}')
