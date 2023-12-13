# %%
import re

txt = open('input.txt').read().splitlines()

# %%
def all_equal(array):
    return all(x == array[0] for x in array)

def derive(array):
    return [b - a for a, b in zip(array[:-1], array[1:])]

def extrapolate(sequence):
    history = [ sequence ]
    while not all_equal(history[-1]):
        history.append(derive(history[-1]))
    return sum(seq[-1] for seq in history)

p1 = 0
p2 = 0
for line in txt:
    sequence = [int(x) for x in re.findall(r'-?\d+', line)]
    p1 += extrapolate(sequence)
    p2 += extrapolate([*reversed(sequence)])

print(f'p1 = {p1}\np1 = {p2}')
