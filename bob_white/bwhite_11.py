"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
"""
from itertools import product

pzl = open("day_11.input").read()


def get_occupied(x, y, grid, *, skip_empty=False):
    vectors = list(product(range(-1, 2), range(-1, 2)))
    vectors.remove((0, 0))
    cnt = 0
    for dx, dy in vectors:
        cx, cy = (dx + x), (dy + y)
        while skip_empty and grid.get((cx, cy), "L") not in ("L", "#"):
            cx += dx
            cy += dy
        cnt += grid.get((cx, cy)) == "#"

    return cnt


def solve_pouzzle(pzl, occupied_number, *, skip_empty=False):
    grid = {(x, y): v for y, line in enumerate(pzl.splitlines()) for x, v in enumerate(line)}
    while True:
        next_grid = grid.copy()
        for (xdx, ydx), val in grid.items():
            occupied = get_occupied(xdx, ydx, grid, skip_empty=skip_empty)
            if val == "L" and not occupied:
                next_grid[(xdx, ydx)] = "#"
            elif val == "#" and occupied >= occupied_number:
                next_grid[(xdx, ydx)] = "L"
        if next_grid == grid:
            break
        grid = next_grid
    return list(grid.values()).count("#")


print(f"Part 01: {solve_pouzzle(pzl, 4)}")
print(f"Part 01: {solve_pouzzle(pzl, 5, skip_empty=True)}")
