# %%
import re
import math
import os
from PIL import Image, ImageDraw
from collections import Counter
from dataclasses import dataclass

txt = [line.strip() for line in open('input.txt').read().splitlines()]

# %%
def integers(line: str) -> list[int]:
    return list(map(int, re.findall(r'-?\d+', line)))

@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int

robots = [Robot(*integers(line)) for line in txt]


# %%
WORLD_MAX_X = 101
WORLD_MAX_Y = 103
WORLD_QUAD_X = WORLD_MAX_X // 2
WORLD_QUAD_Y = WORLD_MAX_Y // 2

def simulate(robot: Robot, time: int) -> Robot:
    x = (robot.x + robot.vx * time) % WORLD_MAX_X
    y = (robot.y + robot.vy * time) % WORLD_MAX_Y
    return Robot(x, y, robot.vx, robot.vy)


# %%
quadrants = Counter()
for robot in robots:
    robot = simulate(robot, 100)
    if robot.x != WORLD_QUAD_X and robot.y != WORLD_QUAD_Y:
        quadrants[(robot.x < WORLD_QUAD_X, robot.y < WORLD_QUAD_Y)] += 1

p1 = math.prod(quadrants.values())
print(f'p1 = {p1}')


# %%
def render(robots: list[Robot]) -> Image:
    img = Image.new('1', (WORLD_MAX_X, WORLD_MAX_Y))
    draw = ImageDraw.Draw(img)
    for robot in robots:
        draw.point((robot.x, robot.y), 1)
    return img


def is_of_interest(time: int) -> bool:
    # magic sauce from observing patterns in rendered images without a filter
    return (time - 28) % WORLD_MAX_X == 0 or (time - 84) % WORLD_MAX_Y == 0


os.makedirs('renders', exist_ok=True)
for t in range(10000):
    if is_of_interest(t):
        img = render([simulate(robot, t) for robot in robots])
        img.save(f'renders/{t}.png')

# %%
