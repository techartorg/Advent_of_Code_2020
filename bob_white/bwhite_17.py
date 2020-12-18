from itertools import product
from collections import defaultdict

pzl = open("day_17.input").read().splitlines()

# Part 1
cube = defaultdict(int) | {(x, y, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)}
directions_01 = [v for v in product((-1, 0, 1), repeat=3) if any(v)]

for _ in range(0, 6):
    new_cube = defaultdict(int)
    for loc in {tuple(sum(v) for v in zip(loc, d)) for loc in cube for d in directions_01 if cube[loc]}:
        active = sum(cube[tuple(sum(v) for v in zip(loc, d))] for d in directions_01)
        new_cube[loc] = cube[loc] and active in (2, 3) or not cube[loc] and active == 3
    cube = new_cube.copy()
print(sum(cube.values()))

# Part 2
hypercube = defaultdict(int) | {(x, y, 0, 0): int(v == "#") for y, line in enumerate(pzl) for x, v in enumerate(line)}
directions_02 = [v for v in product((-1, 0, 1), repeat=4) if any(v)]

for _ in range(0, 6):
    new_cube = defaultdict(int)
    for loc in {tuple(sum(v) for v in zip(loc, d)) for loc in hypercube for d in directions_02 if hypercube[loc]}:
        active = sum(hypercube[tuple(sum(v) for v in zip(loc, d))] for d in directions_02)
        new_cube[loc] = hypercube[loc] and active in (2, 3) or not hypercube[loc] and active == 3
    hypercube = new_cube.copy()
print(sum(hypercube.values()))
