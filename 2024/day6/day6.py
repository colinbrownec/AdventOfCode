# %%
from typing import Self

txt = [[*line.strip()] for line in open('input.txt').read().splitlines()]

def find_char(map, char):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if txt[i][j] == char:
                return [i, j]
start = find_char(txt, '^')

# %%
class DirectionEncoding:
    def __init__(self, name: str, x: int, y: int, mask: int):
        self.name = name
        self.x = x
        self.y = y
        self.mask = mask

    def advance(self, x: int, y: int) -> list[int]:
        return x + self.x, y + self.y

UP = DirectionEncoding('up', -1, 0, 0b0001)
DOWN = DirectionEncoding('down', 1, 0, 0b0010)
LEFT = DirectionEncoding('left', 0, -1, 0b0100)
RIGHT = DirectionEncoding('right', 0, 1, 0b1000)

UP.rotate = RIGHT
RIGHT.rotate = DOWN
DOWN.rotate = LEFT
LEFT.rotate = UP

MAP_BLK = '#'
MAP_OOB = '?'

class LabMap:
    def __init__(self, grid: list[list[chr]]):
        self.grid = grid

    def get(self, x: int, y: int) -> chr:
        if x in range(len(self.grid)) and y in range(len(self.grid[x])):
            return self.grid[x][y]
        return MAP_OOB

    def copy(self) -> Self:
        return LabMap([row.copy() for row in self.grid])

class AlreadyHereException(Exception):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class RecordMap:
    def __init__(self, lab: LabMap):
        self.grid = [[0] * len(row) for row in lab.grid]

    def visit(self, x: int, y: int, direction: DirectionEncoding) -> None:
        if self.grid[x][y] & direction.mask:
            raise AlreadyHereException(x, y)
        self.grid[x][y] |= direction.mask

    def count(self, mask: int) -> int:
        return sum(sum((record & mask) > 0 for record in line) for line in self.grid)

# %%
def travel(grid: LabMap, px: int, py: int, direction = UP, callback = None) -> RecordMap:
    records = RecordMap(grid)

    while grid.get(px, py) != MAP_OOB:
        records.visit(px, py, direction)
        while grid.get(*direction.advance(px, py)) == MAP_BLK:
            direction = direction.rotate
            records.visit(px, py, direction)
        px, py = direction.advance(px, py)
        if callback:
            callback(px, py)

    return records

p1 = travel(LabMap(txt), *start).count(0b01111)
print(f'p1 = {p1}')

# %%
def hypothetical_obstacles(grid: LabMap, px: int, py: int, direction = UP) -> int:
    illegal = [[px, py], direction.advance(px, py)]
    obstacles = []
    def place_obstacle(x: int, y: int):
        nonlocal obstacles
        if [x, y] not in illegal + obstacles and grid.get(x, y) != MAP_OOB:
            hypothetical = grid.copy()
            hypothetical.grid[x][y] = MAP_BLK
            try:
                travel(hypothetical, px, py, direction)
            except AlreadyHereException:
                obstacles.append([x, y])

    travel(grid, px, py, direction, place_obstacle)
    return obstacles

p2 = len(hypothetical_obstacles(LabMap(txt), *start))
print(f'p2 = {p2}')

# %%
