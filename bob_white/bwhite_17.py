from itertools import product
from collections import defaultdict

pzl = open("day_17.input").read().splitlines()

directions = [v for v in product((-1, 0, 1), repeat=4) if any(v)]

# Part 1
cube_01 = defaultdict(int)
cube_01.update({(x, y, 0, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)})

for step in range(1, 7):
    mins = [0 - step, 0 - step, 0 - step, 0]
    maxs = [8 + step, 8 + step, 1 + step, 1]
    new_cube = defaultdict(int)
    for loc in product(*(range(min_, max_) for min_, max_ in zip(mins, maxs))):
        active = sum(cube_01[tuple(sum(v) for v in zip(loc, d))] for d in directions)
        new_cube[loc] = cube_01[loc] and active in (2, 3) or not cube_01[loc] and active == 3
    cube_01 = new_cube.copy()
print(sum(cube_01.values()))


# Part 2
cube_02 = defaultdict(int)
cube_02.update({(x, y, 0, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)})

for step in range(1, 7):
    mins = [0 - step, 0 - step, 0 - step, 0 - step]
    maxs = [8 + step, 8 + step, 1 + step, 1 + step]
    new_cube = defaultdict(int)
    for loc in product(*(range(min_, max_) for min_, max_ in zip(mins, maxs))):
        active = sum(cube_02[tuple(sum(v) for v in zip(loc, d))] for d in directions)
        new_cube[loc] = cube_02[loc] and active in (2, 3) or not cube_02[loc] and active == 3
    cube_02 = new_cube.copy()
print(sum(cube_02.values()))
