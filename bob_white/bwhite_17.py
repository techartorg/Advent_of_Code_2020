from itertools import product
from collections import defaultdict
from typing import Dict, Tuple

pzl = open("day_17.input").read().splitlines()

directions = [v for v in product((-1, 0, 1), repeat=4) if any(v)]

# Part 1
cube: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
for y, line in enumerate(pzl):
    for x, v in enumerate(line):
        cube[(x, y, 0, 0)] = int(v == "#")

for step in range(1, 7):
    mins = [0 - step, 0 - step, 0 - step, 0]
    maxs = [8 + step, 8 + step, 1 + step, 1]
    new_cube: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
    loc: Tuple[int, int, int, int]
    for loc in product(*(range(a, b) for a, b in zip(mins, maxs))):
        active = sum(cube[tuple(sum(v) for v in zip(loc, d))] for d in directions)
        if cube[loc] and active in (2, 3):
            new_cube[loc] = 1
        elif not cube[loc] and active == 3:
            new_cube[loc] = 1
    cube = new_cube.copy()
print(sum(cube.values()))


# Part 2
cube = defaultdict(int)
for y, line in enumerate(pzl):
    for x, v in enumerate(line):
        cube[(x, y, 0, 0)] = int(v == "#")

for step in range(1, 7):
    mins = [0 - step, 0 - step, 0 - step, 0 - step]
    maxs = [8 + step, 8 + step, 1 + step, 1 + step]
    new_cube = defaultdict(int)
    for loc in product(*(range(a, b) for a, b in zip(mins, maxs))):
        active = sum(cube[tuple(sum(v) for v in zip(loc, d))] for d in directions)
        if cube[loc] and active in (2, 3):
            new_cube[loc] = 1
        elif not cube[loc] and active == 3:
            new_cube[loc] = 1
    cube = new_cube.copy()
print(sum(cube.values()))
