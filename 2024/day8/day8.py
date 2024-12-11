# %%
txt = [line.strip() for line in open('input.txt').read().splitlines()]

# %%
m = len(txt)
n = len(txt[0])
def in_bounds(x, y):
    return x in range(m) and y in range(n)

antennae = {}
for i, line in enumerate(txt):
    for j, val in enumerate(line):
        if val == '.':
            continue
        if val not in antennae:
            antennae[val] = []
        antennae[val] += [(i, j)]

def find_antinodes(antennae, limit=False):
    antinodes = set()
    for nodes in antennae.values():
        for i, node in enumerate(nodes):
            for othernode in nodes[i+1:]:
                dx = node[0] - othernode[0]
                dy = node[1] - othernode[1]

                n = 1 if limit else 0
                while in_bounds(node[0] + n * dx, node[1] + n * dy):
                    antinodes.add(f'{node[0] + n * dx} {node[1] + n * dy}')
                    if limit:
                        break
                    n += 1

                n = 1 if limit else 0
                while in_bounds(othernode[0] - n * dx, othernode[1] - n * dy):
                    antinodes.add(f'{othernode[0] - n * dx} {othernode[1] - n * dy}')
                    if limit:
                        break
                    n += 1

    return antinodes

# %%
p1 = len(find_antinodes(antennae, True))
print(f'p1 = {p1}')

# %%
p2 = len(find_antinodes(antennae, False))
print(f'p2 = {p2}')
