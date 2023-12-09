# %%
import math

txt = open('input.txt').read().splitlines()

# %%
directions = txt[0]
paths = { line[0:3]: { 'L': line[7:10], 'R': line[12:15] } for line in txt[2:] }

def follow(source, n = 1):
    for _ in range(n):
        for c in directions:
            source = paths[source][c]
    return source

final_paths = { node: follow(node) for node in paths.keys() }

def distance(source, destination):
    n = 0
    while not source.endswith(destination):
        source = final_paths[source]
        n += 1
    return n

# %%
p1 = distance('AAA', 'ZZZ') * len(directions)
print(f'p1 = {p1}')

# %%
lengths = [ distance(node, 'Z') for node in paths.keys() if node.endswith('A') ]
p2 = math.prod(lengths) * len(directions)
print(f'p2 = {p2}')