# %%
txt = [line.strip() for line in open('input.txt').read().splitlines()]

# %%
FREE_MEMORY = -1
diskmap = list(map(int, txt[0]))

def diskmap_files(diskmap):
    index = 0
    num = 0
    file = True
    files = []
    for val in diskmap:
        if file:
            files.append({ 'value': num, 'index': index, 'size': val})
            num += 1
        file = not file
        index += val
    return files

def memory_layout(files, n):
    memory = [FREE_MEMORY] * n
    for file in files:
        for i in range(file['size']):
            memory[file['index'] + i] = file['value']
    return memory

def checksum(memory):
    return sum(max(0, i * val) for i, val in enumerate(memory))

# %%
def free_p1(diskmap):
    files = diskmap_files(diskmap)
    memory = memory_layout(files, sum(diskmap))

    begin = 0
    end = len(memory) - 1

    while begin < end:
        if memory[end] == FREE_MEMORY:
            end -= 1
            continue

        if memory[begin] != FREE_MEMORY:
            begin += 1
            continue

        memory[begin] = memory[end]
        memory[end] = FREE_MEMORY
        begin += 1
        end -= 1

    return memory

p1 = checksum(free_p1(diskmap))
print(f'p1 = {p1}')

# %%
def free_p2(diskmap):
    files = diskmap_files(diskmap)

    def next_unprocessed():
        return next((file for file in reversed(files) if 'processed' not in file), None)

    while file := next_unprocessed():
        file['processed'] = True
        for i in range(len(files) - 1):
            index = files[i]['index'] + files[i]['size']
            if index > file['index']:
                break
            if files[i+1]['index'] - index >= file['size']:
                file['index'] = index
                files.remove(file)
                files.insert(i+1, file)
                break

    return memory_layout(files, sum(diskmap))

p2 = checksum(free_p2(diskmap))
print(f'p2 = {p2}')

# %%
