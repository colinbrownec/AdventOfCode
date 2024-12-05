# %%
try:
    from tqdm import tqdm
except:
    tqdm = lambda itr: itr

txt = open('input.txt').read().splitlines()

# %%
class GroupRange:
    def __init__(self, span, start = 0):
        self.span = span
        self.start = start
    @property
    def stop(self):
        return self.start + self.span
    def valid(self, record):
        return all(record[i] in '#?' for i in range(self.start,  self.stop))

class PossibleRecords:
    def __init__(self, records, damaged):
        self.records = records
        self.groups = [GroupRange(span) for span in damaged]

    def pack_left(self, n = None):
        if n is None:
            n = len(self.groups)
        for i, g in enumerate(self.groups[:n]):
            g.start = 0 if i == 0 else self.groups[i - 1].stop + 1
            while not g.valid(self.records):
                g.start += 1

    def __repr__(self):
        chars = ['.'] * len(self.records)
        for g in self.groups:
            for i in range(g.start, g.stop):
                chars[i] = '#'
        return ''.join(chars)

    def __iter__(self):
        self.begin = True
        return self

    def __next__(self):
        if self.begin:
            self.begin = False
            self.pack_left()
            return self

        for i, g in enumerate(self.groups):
            if g.stop < len(self.records) and (i + 1 == len(self.groups) or g.stop + 1 < self.groups[i + 1].start):
                g.start += 1
                self.pack_left(i)
                return self

        raise StopIteration

def valid_group(groups, records):
    marks = 0
    for group in groups:
        for i in range(group.start, group.stop):
            if records[i] == '.':
                return False
            if records[i] == '#':
                marks += 1
    return marks == sum(c == '#' for c in records)

# %%
# p1 = 0
# for line in txt:
#     records, damaged = line.split()
#     damaged = [int(n) for n in damaged.split(',')]

#     p1 += sum(valid_group(pg.groups, records) for pg in PossibleRecords(records, damaged))
# print(f'p1 = {p1}')

# %%
# p2 = 0
# for line in tqdm(txt):
#     records, damaged = line.split()
#     damaged = [int(n) for n in damaged.split(',')]

#     records = '?'.join([records] * 5)
#     damaged = damaged * 5

#     p2 += sum(1 for pg in PossibleRecords(records, damaged) if valid_group(pg.groups, records))


line = txt[0]
print(line)
print('-------------')

records, damaged = line.split()
damaged = [int(n) for n in damaged.split(',')]

records = '?'.join([records] * 5)
damaged = damaged * 5

i = 0
for pg in PossibleRecords(records, damaged):
    if i % 1000 == 0:
        print(i, pg)

# print(f'p2 = {p2}')