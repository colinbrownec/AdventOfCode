# %%
from itertools import combinations

txt = open('input.txt').read().splitlines()

# %%
galaxies = []
for y, row in enumerate(txt):
    galaxies += [(x, y) for x, c in enumerate(row) if c == '#']

empty_y = [y for y, row in enumerate(txt) if '#' not in row]
empty_x = [x for x in range(len(txt[0])) if '#' not in (row[x] for row in txt)]

def expand(galaxies, n):
    return [
        (
            x + sum(ex < x for ex in empty_x) * n,
            y + sum(ey < y for ey in empty_y) * n,
        ) for x, y in galaxies
    ]

def distance(galaxy_a, galaxy_b):
    return sum(abs(a - b) for a, b in zip(galaxy_a, galaxy_b))

# %%
p1 = sum(distance(a, b) for a, b in combinations(expand(galaxies, 1), 2))
print(f'p1 = {p1}')

# %%
p2 = sum(distance(a, b) for a, b in combinations(expand(galaxies, 1e6-1), 2))
print(f'p2 = {int(p2)}')
