import re

txt = open('input.txt').readlines()

def to_int(x):
  return int(x) if x.isdigit() else {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  }.get(x)

def calibration(txt, number_pattern):
  sum = 0
  for line in txt:
    nums = [number_pattern.match(line, i) for i in range(len(line))]
    nums = [num.group() for num in nums if num]
    sum += to_int(nums[0]) * 10 + to_int(nums[-1])
  return sum

p1 = calibration(txt, re.compile('[1-9]'))
print(p1)

p2 = calibration(txt, re.compile('[1-9]|one|two|three|four|five|six|seven|eight|nine'))
print(p2)