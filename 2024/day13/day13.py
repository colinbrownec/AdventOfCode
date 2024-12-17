# %%
import re
from copy import deepcopy

txt = [line.strip() for line in open('input.txt').read().splitlines()]


# %%
numbers = re.compile(r'\d+')
machines = []
for i in range(len(txt)):
    if txt[i].startswith('Button A'):
        machines.append({
            'A': list(map(int, numbers.findall(txt[i]))),
            'B': list(map(int, numbers.findall(txt[i + 1]))),
            'prize': list(map(int, numbers.findall(txt[i + 2]))),
        })


# %%
def cost(x, y):
    return x * 3 + y

def cheapest_win(machine):
    possible = []
    def valid(val):
        return val > 0 and val % 1 == 0

    x_num = machine['prize'][0] * machine['B'][1] - machine['prize'][1] * machine['B'][1]
    x_den = machine['A'][0] * machine['B'][1] - machine['A'][1] * machine['B'][0]
    x = x_num / x_den
    y = (machine['prize'][0] - machine['A'][0] * x) / machine['B'][0]

    if valid(x) and valid(y):
        possible.append((int(x), int(y)))

    y_num = machine['prize'][0] * machine['A'][1] - machine['prize'][1] * machine['A'][0]
    y_den = machine['B'][0] * machine['A'][1] - machine['B'][1] * machine['A'][0]
    y = y_num / y_den
    x = (machine['prize'][0] - machine['B'][0] * y) / machine['A'][0]

    if valid(x) and valid(y):
        possible.append((int(x), int(y)))

    if possible:
        return min(possible, key=lambda win: cost(*win))
    return None


# %%
p1 = sum(cost(*win) for win in (cheapest_win(machine) for machine in machines) if win)
print(f'p1 = {p1}')


# %%
p2_machines = deepcopy(machines)
for machine in p2_machines:
    machine['prize'][0] += 10000000000000
    machine['prize'][1] += 10000000000000

p2 = sum(cost(*win) for win in (cheapest_win(machine) for machine in p2_machines) if win)
print(f'p2 = {p2}')


# %%
