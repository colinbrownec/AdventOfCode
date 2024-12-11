# %%
txt = [line.strip() for line in open('input.txt').read().splitlines()]

# %%
def climb(topomap, i, j, visited, height = 0):
    if i not in range(len(topomap)) or j not in range(len(topomap[i])):
        return 0
    if visited is not None and (i, j) in visited:
        return 0
    if topomap[i][j] == str(height):
        if visited is not None:
            visited.add((i, j))
        if topomap[i][j] == '9':
            return 1
        return (
            climb(topomap, i-1, j, visited, height+1) +
            climb(topomap, i+1, j, visited, height+1) +
            climb(topomap, i, j-1, visited, height+1) +
            climb(topomap, i, j+1, visited, height+1)
        )
    return 0

def find_trailheads(topomap):
    trails = []
    for i, line in enumerate(topomap):
        for j, height in enumerate(line):
            if height == '0':
                trails.append({
                    'trailhead': (i, j),
                    'score': climb(topomap, i, j, set()),
                    'rating': climb(topomap, i, j, None),
                })
    return trails

trails = find_trailheads(txt)

# %%
p1 = sum(trail['score'] for trail in trails)
print(f'p1 = {p1}')

p2 = sum(trail['rating'] for trail in trails)
print(f'p2 = {p2}')

# %%
