# %%
txt = open('input.txt').readlines()

# %%
rucksacks = list()
for line in txt:
  items = [ord(c) - (38 if c < 'a' else 96) for c in line.strip()]
  left = items[:len(items) // 2]
  right = items[len(items) // 2:]
  rucksacks += [{ 'items': items, 'left': left, 'right': right }]

# %%
def misplaced(rucksack):
  return next(item for item in rucksack['left'] if item in rucksack['right'])

p1 = sum(misplaced(rucksack) for rucksack in rucksacks)
print(p1)

# %%
def badge(a, b, c):
  return next(item for item in a['items'] if item in b['items'] and item in c['items'])

p2 = sum(badge(*rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3))
print(p2)
