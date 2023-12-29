# %%
txt = open('input.txt').read().split(',')

def HASH(input):
    current_value = 0
    for c in input:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

# %%
p1 = sum(HASH(input) for input in txt)
print(f'p1 = {p1}')

# %%
boxes = dict()
for i in range(256):
    boxes[i] = list()

for command in txt:
    if '=' in command:
        label, focal_length = command.split('=')
        lhash = HASH(label)
        focal_length = int(focal_length)

        if lhash not in boxes:
            boxes[lhash] = [{ 'label': label, 'focal_length': focal_length }]
        else:
            for i, lens in enumerate(boxes[lhash]):
                if lens['label'] == label:
                    lens['focal_length'] = focal_length
                    break
            else:
                boxes[lhash] += [{ 'label': label, 'focal_length': focal_length }]

    else:
        label, _ = command.split('-')
        lhash = HASH(label)

        if lhash in boxes:
            boxes[lhash] = [lens for lens in boxes[lhash] if lens['label'] != label]

def focusing_power(lenses):
    return sum((i + 1) * lens['focal_length'] for i, lens in enumerate(lenses))

p2 = sum((k + 1) * focusing_power(lenses) for k, lenses in boxes.items() if lenses)
print(f'p2 = {p2}')