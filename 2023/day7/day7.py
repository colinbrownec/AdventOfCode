# %%
from itertools import groupby

txt = open('input.txt').read().splitlines()

# %%
def to_card(c):
  if c.isnumeric(): return int(c)
  return { 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }.get(c)

hands = list()
for line in txt:
  cards = [to_card(c) for c in line[:5]]
  hands.append({
    'cards': cards,
    'bid': int(line[5:]),
    'groups': sorted(
      [len(list(g)) for k, g in groupby(sorted(cards))],
      reverse=True),
  })

hands.sort(key=lambda hand: hand['groups'] + hand['cards'])
p1 = sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands))
print(p1)
  
# %%
def to_card(c):
  if c.isnumeric(): return int(c)
  return { 'T': 10, 'J': 0, 'Q': 12, 'K': 13, 'A': 14 }.get(c)

hands = list()
for line in txt:
  cards = [to_card(c) for c in line[:5]]
  njcards = [c for c in cards if c != to_card('J')]
  jokers = len(cards) - len(njcards)
  
  groups = sorted(
    [len(list(g)) for k, g in groupby(sorted(njcards))],
    reverse=True)
  
  if groups:
    groups[0] += jokers
  else:
    groups = [jokers]
  
  hands.append({
    'cards': cards,
    'bid': int(line[5:]),
    'groups': groups,
  })

hands.sort(key=lambda hand: hand['groups'] + hand['cards'])
p1 = sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands))
print(p1)