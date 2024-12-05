# %%
import re

txt = open('input.txt').read().splitlines()

# %%
pairs = list()
p1 = 0
p2 = 0
for line in txt:
  a_start, a_stop, b_start, b_stop = map(int, re.findall(r'\d+', line))
  if (a_start <= b_start and b_stop <= a_stop) or (b_start <= a_start and a_stop <= b_stop):
    p1 += 1
  if (a_start <= b_start and b_start <= a_stop) or (b_start <= a_start and a_start <= b_stop):
    p2 += 1

print(p1)
print(p2)