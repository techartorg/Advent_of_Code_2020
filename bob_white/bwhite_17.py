from itertools import product
from collections import defaultdict

pzl = open("day_17.input").read().splitlines()

# Part 1
cube_01 = defaultdict(int)
cube_01.update({(x, y, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)})
directions_01 = [v for v in product((-1, 0, 1), repeat=3) if any(v)]

for _ in range(0, 6):
    new_cube = defaultdict(int)
    for loc in {tuple(sum(v) for v in zip(loc, d)) for loc in cube_01 for d in directions_01 if cube_01[loc]}:
        active = sum(cube_01[tuple(sum(v) for v in zip(loc, d))] for d in directions_01)
        new_cube[loc] = cube_01[loc] and active in (2, 3) or not cube_01[loc] and active == 3
    cube_01 = new_cube.copy()
print(sum(cube_01.values()))

# Part 2
cube_02 = defaultdict(int)
cube_02.update({(x, y, 0, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)})
directions_02 = [v for v in product((-1, 0, 1), repeat=4) if any(v)]

cube_02 = defaultdict(int)
cube_02.update({(x, y, 0, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)})
for _ in range(0, 6):
    new_cube = defaultdict(int)
    for loc in {tuple(sum(v) for v in zip(loc, d)) for loc in cube_02 for d in directions_02 if cube_02[loc]}:
        active = sum(cube_02[tuple(sum(v) for v in zip(loc, d))] for d in directions_02)
        new_cube[loc] = cube_02[loc] and active in (2, 3) or not cube_02[loc] and active == 3
    cube_02 = new_cube.copy()
print(sum(cube_02.values()))
