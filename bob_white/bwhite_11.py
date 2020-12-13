"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
"""
from itertools import product

pzl = open("day_11.input").read()


def get_occupied(loc, grid, *, skip_empty=False):
    vectors = list(s for v in product([-1, 0, 1], [-1j, 0j, 1j]) if (s := sum(v)))
    cnt = 0
    for v in vectors:
        dv = v + loc
        while skip_empty and grid.get(dv, "L") not in ("L", "#"):
            dv += v

        cnt += grid.get(dv) == "#"
    return cnt


def solve_pouzzle(pzl, occupied_number, *, skip_empty=False):
    grid = {(x + (y * -1j)): v for y, line in enumerate(pzl.splitlines()) for x, v in enumerate(line)}
    while True:
        next_grid = grid.copy()
        for loc, val in grid.items():
            occupied = get_occupied(loc, grid, skip_empty=skip_empty)
            if val == "L" and not occupied:
                next_grid[loc] = "#"
            elif val == "#" and occupied >= occupied_number:
                next_grid[loc] = "L"
        if next_grid == grid:
            break
        grid = next_grid
    return list(grid.values()).count("#")


print(f"Part 01: {solve_pouzzle(pzl, 4)}")
print(f"Part 01: {solve_pouzzle(pzl, 5, skip_empty=True)}")
