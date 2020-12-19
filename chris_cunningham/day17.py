from collections import defaultdict
from itertools import product
from typing import NamedTuple, Iterable

from utils import timer

_TEST_DATA = """.#.
..#
###"""


class Vector(NamedTuple):
    x: int
    y: int
    z: int = 0
    w: int = 0

    def __add__(self, other):
        return type(self)(*(a + b for a, b in zip(self, other)))


Grid = defaultdict[Vector, bool]


def parse_grid() -> Grid:
    with open("inputs/day17.txt", 'r') as f:
        grid: Grid = defaultdict(bool)

        for y, line in enumerate(f.read().splitlines()):
            for x, value in enumerate(line):
                if value == "#":
                    grid[Vector(x, y)] = True

        return grid


def get_neighbours(start_vector: Vector, dimensions: int) -> Iterable[Vector]:
    return (start_vector + Vector(*d) for d in product(range(-1, 2), repeat=dimensions) if any(d))


@timer(1)
def solve(dimensions: int) -> int:
    grid = parse_grid()

    for _ in range(6):
        new_grid = defaultdict(bool)

        # expand grid out around active
        for vec in [k for k, v in grid.items() if v]:
            new_grid |= {i: grid[i] for i in get_neighbours(vec, dimensions)}

        for vec, value in new_grid.items():
            active_count = sum(grid[i] for i in get_neighbours(vec, dimensions))

            if value and active_count not in (2, 3):
                new_grid[vec] = False
            elif not value and active_count == 3:
                new_grid[vec] = True

        grid = defaultdict(bool, {k: v for k, v in new_grid.items() if v})

    return sum(grid.values())


print(f"part a: {solve(3)}")
print(f"part b: {solve(4)}")

