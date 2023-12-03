import re
import math

txt = open('input.txt').readlines()

symbol_pattern = re.compile('[^.0-9]')
number_pattern = re.compile('\d+')

symbols = []
numbers = []

for row, line in enumerate(txt):
  symbols += [{ 'y': row, 'x': symbol.span()[0], 'val': symbol.group() } for symbol in symbol_pattern.finditer(line.strip())]
  numbers += [{ 'y': row, 'xspan': number.span(), 'val': int(number.group()) } for number in number_pattern.finditer(line.strip())]

def is_adjacent(number, symbol):
  near_y = abs(number['y'] - symbol['y']) <= 1
  near_x = any([abs(col - symbol['x']) <= 1 for col in range(*number['xspan'])])
  return near_x and near_y

p1 = sum(number['val'] for number in numbers if any(is_adjacent(number, symbol) for symbol in symbols))
print(p1)

p2 = 0
for symbol in symbols:
  adjacent = [number['val'] for number in numbers if is_adjacent(number, symbol)]
  if symbol['val'] == '*' and len(adjacent) == 2:
    p2 += math.prod(adjacent)
print(p2)
