# %%
txt = open('input.txt').readlines()

# %%
class Rucksack:
  def __init__(self, line):
    self.items = [ord(c) - (38 if c < 'a' else 96) for c in line]
  def left(self): return self.items[:len(self.items) // 2]
  def right(self): return self.items[len(self.items) // 2:]
rucksacks = [Rucksack(line.strip()) for line in txt]

# %%
def misplaced(rucksack):
  return next(item for item in rucksack.left() if item in rucksack.right())

p1 = sum(misplaced(rucksack) for rucksack in rucksacks)
print(p1)

# %%
def badge(a, b, c):
  return next(item for item in a.items if item in b.items and item in c.items)

p2 = sum(badge(*rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3))
print(p2)
