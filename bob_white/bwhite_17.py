from itertools import product
from collections import defaultdict

pzl = open("day_17.input").read().splitlines()

# Part 1
cube: dict[tuple, int] = defaultdict(int) | {(x, y, 0): True for y, line in enumerate(pzl) for x, v in enumerate(line) if v == "#"}
directions_3d = [v for v in product((-1, 0, 1), repeat=3) if any(v)]
# Part 2
hypercube: dict[tuple, int] = defaultdict(int) | {(x, y, 0, 0): True for y, line in enumerate(pzl) for x, v in enumerate(line) if v == "#"}
directions_4d = [v for v in product((-1, 0, 1), repeat=4) if any(v)]

for _ in range(0, 6):
    new_cube: dict[tuple, int] = defaultdict(int) | {
        loc: True
        for loc in {tuple(sum(v) for v in zip(loc, d)) for loc in cube for d in directions_3d if cube[loc]}
        if (active := sum(cube[tuple(sum(v) for v in zip(loc, d))] for d in directions_3d)) and (cube[loc] and active in (2, 3) or not cube[loc] and active == 3)
    }
    new_hypercube: dict[tuple, int] = defaultdict(int) | {
        loc: True
        for loc in {tuple(sum(v) for v in zip(loc, d)) for loc in hypercube for d in directions_4d if hypercube[loc]}
        if (active := sum(hypercube[tuple(sum(v) for v in zip(loc, d))] for d in directions_4d))
        and (hypercube[loc] and active in (2, 3) or not hypercube[loc] and active == 3)
    }
    cube = new_cube.copy()
    hypercube = new_hypercube.copy()
print(sum(cube.values()))
print(sum(hypercube.values()))
