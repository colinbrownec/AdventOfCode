from dataclasses import dataclass, field
from functools import reduce

txt = open('input.txt').readlines()

@dataclass
class Elf:
  food: list[int] = field(default_factory=list)

def parse(arr, line):
  if line.strip().isdigit(): arr[-1].food.append(int(line))
  else: arr.append(Elf())
  return arr

elves = reduce(parse, txt, [Elf()])

p1 = max(sum(elf.food) for elf in elves)
print(p1)

p2 = sum(sorted((sum(elf.food) for elf in elves), reverse=True)[:3])
print(p2)