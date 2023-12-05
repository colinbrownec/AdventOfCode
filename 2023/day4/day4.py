# %%
from itertools import repeat

txt = open('input.txt').readlines()

# %%
wins = []
for line in txt:
  game, results = line.split(':')
  winning, selected = results.split('|')

  winning = [int(v) for v in winning.split()]
  selected = [int(v) for v in selected.split()]

  wins.append(sum(num in winning for num in selected))

# %%
p1 = sum(2 ** (n - 1) if n > 0 else 0 for n in wins)
print(p1)

# %%
copies = list(repeat(1, len(wins)))
for i, n in enumerate(wins):
  for index in range(i, i + n):
    copies[index + 1] += copies[i]

p2 = sum(copies)
print(p2)