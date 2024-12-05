# %%
txt = open('input.txt').read().splitlines()

# %%
left = []
right = []
for line in txt:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

# %%
def distance(left, right):
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

def similarity(left, right):
    weights = {}
    for v in right:
        if v in weights:
            weights[v] += 1
        else:
            weights[v] = 1

    total = 0
    for v in left:
        if v in weights:
            total += v * weights[v]

    return total

# %%
p1 = distance(left, right)
print(f'p1 = {p1}')

# %%
p2 = similarity(left, right)
print(f'p2 = {p2}')

# %%
