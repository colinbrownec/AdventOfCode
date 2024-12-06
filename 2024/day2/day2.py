# %%
txt = open('input.txt').readlines()

# %%
reports = [list(map(int, line.split())) for line in txt]

# %%
def safe(level):
    increasing = level[0] < level[1]
    for i in range(len(level) - 1):
        if increasing and (level[i] >= level[i + 1]):
            return False
        if not increasing and (level[i] <= level[i + 1]):
            return False
        if abs(level[i] - level[i + 1]) not in range(1, 4):
            return False
    return True

p1 = sum(safe(level) for level in reports)
print(f'p1 = {p1}')

# %%
def almost_safe(level):
    if safe(level):
        return True
    for i in range(len(level)):
        if safe(level[:i] + level[i+1:]):
            return True
    return False

p2 = sum(almost_safe(level) for level in reports)
print(f'p2 = {p2}')

# %%
