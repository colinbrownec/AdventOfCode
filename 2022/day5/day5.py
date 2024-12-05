# %%
from itertools import batched

txt = open('input.txt').read().splitlines()

# %%
txts = iter(txt)
stacks = [list() for i in range((len(txt[0]) + 1) // 4)]

while line := next(txts, None):
  if '[' in line:
    for i, crate in enumerate(batched(line, 4)):
      if crate[1].isalpha():
        stacks[i].append(crate[1])
  else:
    break

print(line)

while line := next(txts, None):
  print(line)

print(stacks)
# %%
