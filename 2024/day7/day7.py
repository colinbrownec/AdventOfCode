# %%
import itertools

txt = open('input.txt').read().splitlines()

def parse(line):
    value, inputs = line.split(':')
    return {
        'value': int(value),
        'inputs': list(map(int, inputs.split()))
    }

equations = list(map(parse, txt))

# %%
def do_op(a, b, op):
    if op == '*': return a * b
    if op == '+': return a + b
    if op == '|': return int(str(a) + str(b))
    raise RuntimeError()

def evaluate(inputs, operations):
    val = inputs[0]
    for i, op in enumerate(operations):
        val = do_op(val, inputs[i+1], op)
    return val

def is_possible(inputs, target_value, operations):
    for ops in itertools.product(operations, repeat=len(inputs)-1):
        if evaluate(inputs, ops) == target_value:
            return True
    return False

# %%
p1 = sum(eq['value'] for eq in equations if is_possible(eq['inputs'], eq['value'], '+*'))
print(f'p1 = {p1}')

p2 = sum(eq['value'] for eq in equations if is_possible(eq['inputs'], eq['value'], '+*|'))
print(f'p2 = {p2}')

# %%
