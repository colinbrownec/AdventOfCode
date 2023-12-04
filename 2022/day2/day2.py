from enum import Enum
from dataclasses import dataclass

txt = open('input.txt').readlines()

Play = Enum('Play', ['Rock', 'Paper', 'Scissors'])
plays = { 
  'A': Play.Rock, 'B': Play.Paper, 'C': Play.Scissors,
  'X': Play.Rock, 'Y': Play.Paper, 'Z': Play.Scissors,
}

@dataclass
class Game:
  opponent: Play
  player: Play
  def score(self) -> int:
    if self.opponent == self.player:
      return self.player.value + 3
    match (self.opponent, self.player):
      case (Play.Rock, Play.Paper) | (Play.Paper, Play.Scissors) | (Play.Scissors, Play.Rock):
        return self.player.value + 6
    return self.player.value

def parse_p1_game(line):
  o, p = line.split()
  return Game(plays[o], plays[p])

p1_games = [parse_p1_game(line) for line in txt]
p1 = sum(game.score() for game in p1_games)
print(p1)

wins_against = {
    Play.Rock: Play.Paper,
    Play.Paper: Play.Scissors,
    Play.Scissors: Play.Rock,    
}

def parse_p2_game(line):
  o, result = line.split()
  opponent = plays[o]
  if result == 'X':
    return Game(opponent, next(play for play in Play if wins_against[play] == opponent))
  if result == 'Y':
    return Game(opponent, opponent)
  if result == 'Z':
    return Game(opponent, wins_against[opponent])

p2_games = [parse_p2_game(line) for line in txt]
p2 = sum(game.score() for game in p2_games)
print(p2)