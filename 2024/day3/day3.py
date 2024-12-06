# %%
import re

txt = open('input.txt').readlines()

# %%
memory = ''.join(txt)

def evalulate(instrs):
    return sum(int(a) * int(b) for (a, b) in instrs)

# %%
mul = r'mul\((\d+),(\d+)\)'

instrs = re.findall(mul, memory)

p1 = evalulate(instrs)
print(f'p1 = {p1}')

# %%
do = r'do\(\)'
dont = r'don\'t\(\)'

all_instrs = re.findall(f'{mul}|({do})|({dont})', memory)

enabled = True
enabled_instrs = []
for instr in all_instrs:
    if instr[2]:
        enabled = True
    elif instr[3]:
        enabled = False
    elif enabled:
        enabled_instrs.append(instr[:2])

p2 = evalulate(enabled_instrs)
print(f'p2 = {p2}')

# %%
