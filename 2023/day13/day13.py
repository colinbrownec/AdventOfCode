from itertools import groupby

txt = open('input.txt').read().splitlines()

patterns = [list(g) for k, g in groupby(txt, lambda line: len(line)) if k]
def reflects_y(pattern, y):
    differences = 0
    y_lesser = y
    y_greater = y + 1

    while y_lesser >= 0 and y_greater < len(pattern):
        differences += sum(a != b for a, b in zip(pattern[y_lesser], pattern[y_greater]))
        y_lesser -= 1
        y_greater += 1
    return differences

def transpose(pattern):
    return [''.join(row) for row in zip(*pattern)]

def find_reflection(pattern, differences):
    for y in range(0, len(pattern) - 1):
        if reflects_y(pattern, y) == differences:
            return ('y', y)

    pattern = transpose(pattern)

    for x in range(0, len(pattern) - 1):
        if reflects_y(pattern, x) == differences:
            return ('x', x)

    return (None, None)

def score(direction, index):
    return (index + 1) * (1 if direction == 'x' else 100)

pl = sum(score(*find_reflection(p, 0)) for p in patterns)
print(f'pl = {pl}')

p2 = sum(score(*find_reflection(p, 1)) for p in patterns)
print(f'p2 = {p2}')