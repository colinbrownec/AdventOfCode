import re

pattern = re.compile('[1-9]|one|two|three|four|five|six|seven|eight|nine')

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

sum = 0
for w in open('input.txt').readlines():
  nums = [pattern.match(w, i) for i in range(len(w))]
  nums = [num.group(0) for num in nums if num]

  sum += to_int(nums[0]) * 10 + to_int(nums[-1])

print(sum)