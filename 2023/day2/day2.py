import re

txt = open('input.txt').readlines()

game_pattern = re.compile('Game (\d+):')
cube_pattern = re.compile('(\d+) (red|blue|green)')

def parse_game(txt):
  game = int(game_pattern.match(txt).group(1))
  draws = [{ color:int(count) for count, color in cube_pattern.findall(draw) } for draw in txt.split(';')]
  return { 'id': game, 'draws': draws }

games = [parse_game(line) for line in txt]

def possible_game(game, colors):
  for draw in game['draws']:
    for color, count in colors.items():
      if draw.get(color, 0) > count: return False
  return True

expected = { 'red': 12, 'green': 13, 'blue': 14 }
p1 = sum(game['id'] for game in games if possible_game(game, expected))
print(p1)

def game_power(game):
  r = max(draw.get('red', 0)   for draw in game['draws'])
  g = max(draw.get('green', 0) for draw in game['draws'])
  b = max(draw.get('blue', 0)  for draw in game['draws'])
  return r * g * b

p2 = sum(game_power(game) for game in games)
print(p2)