# %%
txt = [line.strip() for line in open("input.txt").read().splitlines()]


# %%
def fill(
    plants: list[str],
    x: int,
    y: int,
    target: chr,
    region: list[(int, int)],
) -> list[(int, int)]:
    if x not in range(len(plants)) or y not in range(len(plants[x])):
        return region
    if plants[x][y] != target:
        return region
    if (x, y) in region:
        return region

    region.append((x, y))
    fill(plants, x - 1, y, target, region)
    fill(plants, x + 1, y, target, region)
    fill(plants, x, y - 1, target, region)
    fill(plants, x, y + 1, target, region)
    return region


class Plot:
    def __init__(self, plants: list[str], plant: chr, region: list[(int, int)]):
        self.plants = plants
        self.plant = plant
        self.region = region

    def fences(self) -> list[tuple[chr, float, int]]:
        found = []

        def is_other_plant(x: int, y: int) -> int:
            if x not in range(len(self.plants)) or y not in range(len(self.plants[x])):
                return True
            return self.plants[x][y] != self.plant

        for x, y in self.region:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if is_other_plant(x + dx, y + dy):
                    if abs(dx):
                        found.append(('x', x + dx / 4, y))
                    else:
                        found.append(('y', y + dy / 4, x))
        return found

    def perimiter(self) -> int:
        return len(self.fences())

    def area(self) -> int:
        return len(self.region)

    def sides(self) -> int:
        grouped = {}
        for axis, index, position in self.fences():
            if (axis, index) not in grouped:
                grouped[(axis, index)] = []
            grouped[(axis, index)].append(position)

        sides = 0
        for (axis, index), positions in grouped.items():
            groups = 1
            positions.sort()
            prev_pos = positions[0]
            for pos in positions[1:]:
                if pos != prev_pos + 1:
                    groups += 1
                prev_pos = pos
            sides += groups
        return sides


# %%
def find_plots(plants: list[str]) -> list[Plot]:
    plots = []
    visited = []
    for i in range(len(plants)):
        for j in range(len(plants[i])):
            if (i, j) not in visited:
                region = fill(plants, i, j, plants[i][j], [])
                plots.append(Plot(plants, plants[i][j], region))
                visited.extend(region)
    return plots


plots = find_plots(txt)


# %%
p1 = sum(plot.perimiter() * plot.area() for plot in plots)
print(f"p1 = {p1}")

p2 = sum(plot.sides() * plot.area() for plot in plots)
print(f"p2 = {p2}")


# %%
