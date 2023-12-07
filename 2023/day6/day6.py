# %%
import re
import math

txt = open('input.txt').read().splitlines()

# %%
# given t and d:
# t_up + t_down = t
# t_down * t_up > d
#
# rewrite:
# t_up = t - t_down
#
# substitute:
# t_down * (t - t_down) = d
# -t_down ** 2 + t * t_down - d = 0
#
# note:
# a * x**2 + b * x + c = 0
# a = -1
# b = t
# c = -d
#
# solve:
# t_down = (-t +/- sqrt(t ** 2 - 4 * -1 * -d)) / (2 * -1)
# t_down = (t +/- sqrt(t ** 2 - 4 * d)) / 2

def solve(t, d):
  sqrt = math.sqrt(t ** 2 - 4 * d)
  a = (t + sqrt) / 2
  b = (t - sqrt) / 2
  return a, b

def possible_wins(t, d):
  a, b = solve(t, d)
  if b < a:
    a, b = b, a
  return math.floor(b) - math.ceil(a) + 1

# %%
times = [int(t.group()) for t in re.finditer(r'\d+', txt[0])]
distances = [int(d.group()) for d in re.finditer(r'\d+', txt[1])]

p1 = math.prod(possible_wins(t, d) for t, d in zip(times, distances))
print(p1)

# %%
t = int(re.search(r'\d+', re.sub(r'\s', '', txt[0])).group())
d = int(re.search(r'\d+', re.sub(r'\s', '', txt[1])).group())

p2 = possible_wins(t, d)
print(p2)