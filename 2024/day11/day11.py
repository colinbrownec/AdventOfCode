# %%
from collections import Counter

txt = [line.strip() for line in open('input.txt').read().splitlines()]

# %%
stones = list(map(int, txt[0].split()))

def blink(stones):
    newstones = Counter()
    for num, count in stones.items():
        if num == 0:
            newstones[1] += count
            continue
        strnum = str(num)
        if len(strnum) % 2 == 0:
            newstones[int(strnum[:len(strnum)//2])] += count
            newstones[int(strnum[len(strnum)//2:])] += count
        else:
            newstones[num * 2024] += count
    return newstones

def blink_n(starting_stones, n):
    stones = Counter()
    for num in starting_stones:
        stones[num] += 1

    for _ in range(n):
        stones = blink(stones)

    return stones

# %%
p2 = sum(blink_n(stones, 25).values())
print(f'p2 = {p2}')

p2 = sum(blink_n(stones, 75).values())
print(f'p2 = {p2}')