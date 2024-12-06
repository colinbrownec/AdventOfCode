# %%
txt = open('input.txt').readlines()

# %%
rules = {}
updates = []

for line in txt:
    if '|' in line:
        before, after = map(int, line.split('|'))
        if before in rules:
            rules[before].append(after)
        else:
            rules[before] = [after]
    elif ',' in line:
        updates.append(list(map(int, line.split(','))))

# %%
def is_ordered(update):
    processed = []
    for page in update:
        processed.append(page)
        if page not in rules:
            continue
        for after in rules[page]:
            if after in processed:
                return False
    return True

p1 = sum(update[len(update)//2] for update in updates if is_ordered(update))
print(f'p1 = {p1}')

# %%
def make_ordered(update):
    while not is_ordered(update):
        processed = []
        for page in update:
            processed.append(page)
            if page not in rules:
                continue
            for after in rules[page]:
                if after in processed:
                    processed.remove(after)
                    processed.append(after)
        update = processed
    return update

def score(update):
    if not is_ordered(update):
        update = make_ordered(update)
        return update[len(update)//2]
    return 0

p2 = sum(score(update) for update in updates)
print(f'p2 = {p2}')

# %%
