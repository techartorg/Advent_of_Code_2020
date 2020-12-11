"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
"""
from pprint import pprint
from itertools import product

pzl = open("day_11.input").read()
vectors = list(product(range(-1, 2), range(-1, 2)))
vectors.remove((0, 0))


def get_occupied(x, y, grid):
    cnt = 0
    vals = []
    for dx, dy in vectors:
        cx, cy = (dx + x), (dy + y)
        if not (0 <= cx < len(grid[0])) or not (0 <= cy < len(grid)):
            continue

        cnt += grid[dy + y][dx + x] == "#"
        vals.append(grid[dy + y][dx + x])

    return cnt


while True:
    old_pzl = pzl
    grid = [[c for c in line] for line in pzl.splitlines()]
    new_grid = [line[:] for line in grid]
    for ydx, line in enumerate(grid):
        for xdx, val in enumerate(line):
            occupied = get_occupied(xdx, ydx, grid)
            if val == "L" and not occupied:
                new_grid[ydx][xdx] = "#"
            elif val == "#" and occupied >= 4:
                new_grid[ydx][xdx] = "L"
    pzl = "\n".join("".join(line) for line in new_grid)
    if old_pzl == pzl:
        break

print(f'Part 01: {pzl.count("#")}')
pzl = open("day_11.input").read()


def get_occupied2(x, y, grid):
    cnt = 0
    for dx, dy in vectors:
        cx = dx + x
        cy = dy + y
        try:
            while grid[cy][cx] not in ("#", "L"):
                cx += dx
                cy += dy

        except IndexError:
            pass
        else:
            if not 0 <= cx < len(grid[0]):
                continue
            if not 0 <= cy < len(grid):
                continue
            cnt += grid[cy][cx] == "#"

    return cnt


while True:
    old_pzl = pzl

    grid = [[c for c in line] for line in pzl.splitlines()]
    new_grid = [line[:] for line in grid]
    for ydx, line in enumerate(grid):
        for xdx, val in enumerate(line):
            occupied = get_occupied2(xdx, ydx, grid)
            if val == "L" and not occupied:
                new_grid[ydx][xdx] = "#"
            elif val == "#" and occupied >= 5:
                new_grid[ydx][xdx] = "L"
    pzl = "\n".join("".join(line) for line in new_grid)
    if old_pzl == pzl:
        break
print(f'Part 02: {pzl.count("#")}')
