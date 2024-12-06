# %%
import re

txt = [line.strip() for line in open('input.txt').readlines()]

# %%
def rotate_90(lines):
    rlines = []
    for i in range(len(lines[0])):
        line = ''
        for j in reversed(range(len(lines))):
            line += lines[j][i]
        rlines.append(line)
    return rlines

def rotate_45(lines):
    rlines = []

    def diagonal(x, y):
        line = ''
        while True:
            line += lines[x][y]
            x += 1
            y += 1
            if x >= len(lines) or y >= len(lines[x]):
                break
        return line

    for i in range(len(lines)):
        rlines.append(diagonal(i, 0))
    for j in range(1, len(lines[0])):
        rlines.append(diagonal(0, j))
    return rlines

# %%
xmas = re.compile('XMAS')
samx = re.compile('SAMX')

def count_xmas_p1(lines):
    count = 0
    for line in lines:
        count += len(xmas.findall(line))
        count += len(samx.findall(line))
    return count

p1 = sum([
    count_xmas_p1(txt),
    count_xmas_p1(rotate_90(txt)),
    count_xmas_p1(rotate_45(txt)), 
    count_xmas_p1(rotate_45(rotate_90(txt)))
])
print(f'p1 = {p1}')

# %%
locations = ((-1, -1), (1, 1), (1, -1), (-1, 1))
valid = ('MSMS', 'MSSM', 'SMMS', 'SMSM')

def count_xmas_p2(lines):
    count = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] == 'A':
                neighbors = ''.join(lines[i+x][j+y] for x, y in locations)
                if neighbors in valid:
                    count += 1
    return count

p2 = count_xmas_p2(txt)
print(f'p2 = {p2}')

# %%
