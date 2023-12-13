# %%
try:
    from tqdm import tqdm
except:
    tqdm = lambda itr: itr

txt = open('input.txt').read().splitlines()

# %%
pipes = '|-LJ7F'

def connects(pipe, direction):
    if direction == 'LEFT':
        return pipe in '-J7'
    if direction == 'RIGHT':
        return pipe in '-LF'
    if direction == 'UP':
        return pipe in '|LJ'
    if direction == 'DOWN':
        return pipe in '|7F'

def opposite(direction):
    if direction == 'LEFT':
        return 'RIGHT'
    if direction == 'RIGHT':
        return 'LEFT'
    if direction == 'UP':
        return 'DOWN'
    if direction == 'DOWN':
        return 'UP'

def lookup(x, y):
    char = txt[y][x]
    if char in pipes: return char

    has_l = x - 1 >= 0          and connects(txt[y][x - 1], 'RIGHT')
    has_r = x + 1 < len(txt)    and connects(txt[y][x + 1], 'LEFT')
    has_u = y - 1 >= 0          and connects(txt[y - 1][x], 'DOWN')
    has_d = y + 1 < len(txt[0]) and connects(txt[y + 1][x], 'UP')

    if has_l and has_r:
        return '-'
    if has_u and has_d:
        return '|'
    if has_l and has_u:
        return 'J'
    if has_l and has_d:
        return '7'
    if has_r and has_u:
        return 'L'
    if has_r and has_d:
        return 'F'

for y, row in enumerate(txt):
    if 'S' in row:
        (sx, sy) = (row.index('S'), y)

# %%
def crawl(x, y, direction = None):
    pipe = lookup(x, y)
    direction = next(d for d in { 'UP', 'DOWN', 'LEFT', 'RIGHT' } - { opposite(direction) } if connects(pipe, d))
    if direction == 'LEFT':
        return (x - 1, y), direction
    if direction == 'RIGHT':
        return (x + 1, y), direction
    if direction == 'UP':
        return (x, y - 1), direction
    if direction == 'DOWN':
        return (x, y + 1), direction

loop = [(sx, sy)]

(cx, cy) = (sx, sy)
(cx, cy), direction = crawl(cx, cy)

while (cx, cy) != (sx, sy):
    loop += [(cx, cy)]
    (cx, cy), direction = crawl(cx, cy, direction)

p1 = len(loop) // 2
print(f'p1 = {p1}')

# %%
def count_up_pipes(x, y):
    n = 0
    for xx in range(x):
        if (xx, y) in loop and connects(lookup(xx, y), 'UP'):
            n += 1
    return n

p2 = 0
for y in tqdm(range(len(txt))):
    for x in range(len(txt[0])):
        if (x, y) not in loop:
            if count_up_pipes(x, y) % 2 == 1:
                p2 += 1

print(f'p2 = {p2}')
