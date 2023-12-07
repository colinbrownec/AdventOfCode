# %%
from bisect import bisect
from dataclasses import dataclass
import re
import math

txt = open('input.txt').read().splitlines()

# %%
def ints(line):
  return list(map(int, re.findall(r'\d+', line)))

@dataclass
class Range:
  destination_start: int
  source_start: int
  n: int

itr = iter(txt)
seeds = ints(next(itr))
maps = dict()

while True:
  try:
    line = next(itr)
    if len(line) == 0:
      name = re.search(r'(.*) map:', next(itr)).group(1)
      maps[name] = list()
    else:
      maps[name].append(Range(*ints(line)))
  except StopIteration:
    break

# sort map Ranges so we can search with bisect
for ranges in maps.values():
  ranges.sort(key=lambda x: x.source_start)

def use_map(mapping, value):
  ip = bisect(mapping, value, key=lambda x: x.source_start + x.n)

  if ip < len(mapping):
    mrange = mapping[ip]
    if mrange.source_start <= value:
      return value - mrange.source_start + mrange.destination_start
  return value

  # try:
  #   return next(m for m in mapping if m.map(value)).map(value)
  # except StopIteration:
  #   return value

def seed_to_location(seed):
  tmp = use_map(maps['seed-to-soil'], seed)
  tmp = use_map(maps['soil-to-fertilizer'], tmp)
  tmp = use_map(maps['fertilizer-to-water'], tmp)
  tmp = use_map(maps['water-to-light'], tmp)
  tmp = use_map(maps['light-to-temperature'], tmp)
  tmp = use_map(maps['temperature-to-humidity'], tmp)
  return use_map(maps['humidity-to-location'], tmp)

# %%
p1 = min(seed_to_location(seed) for seed in seeds)
print(p1)

# %%
p2 = math.inf
for i in range(0, len(seeds), 2):
  for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
    p2 = min(p2, seed_to_location(seed))

print(p2)
