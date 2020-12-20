from math import prod
from collections import defaultdict
from itertools import product

pzl_input = open("day_20.input").read().split("\n\n")

tiles: defaultdict[int, list[str]] = defaultdict(list)
for block in pzl_input:
    title, *t = block.splitlines()
    tiles[int(title[len("Tile ") : -1])] = t


def print_tile(title, contents):
    print("")
    print(title)
    print("\n".join(line for line in contents))


def find_edges(tile: list[str]):
    top = find_top(tile)
    bottom = find_bottom(tile)
    left = find_left(tile)
    right = find_right(tile)
    return {top, bottom, left, right}


def find_right(tile):
    return "".join(line[-1] for line in tile)


def find_left(tile):
    return "".join(line[0] for line in tile)


def find_bottom(tile):
    return tile[-1]


def find_top(tile):
    return tile[0]


def find_all_edges(tile: list[str]):
    return find_edges(tile) | {edge[::-1] for edge in find_edges(tile)}


def flip_v(tile: list[str]):
    tile[:] = tile[::-1]


def flip_h(tile: list[str]):
    tile[:] = [line[::-1] for line in tile]


def transpose_tile(tile: list[str]):
    tile[:] = ["".join(z) for z in zip(*tile)]


def rotate(tile: list[str]):
    flip_h(tile)
    transpose_tile(tile)


connections = defaultdict(set)
for tile in tiles.items():
    title, contents = tile
    for other_tile in tiles.items():
        other_title, other_contents = other_tile
        if tile == other_tile:
            continue
        for edge in find_all_edges(tile[1]):
            if edge in find_all_edges(other_tile[1]):
                connections[title].add(other_title)

corner_tiles = {k: v for k, v in connections.items() if len(v) == 2}
edge_tiles = {k: v for k, v in connections.items() if len(v) == 3}
center_tiles = {k: v for k, v in connections.items() if len(v) == 4}

print(f"Part 01: {prod(corner_tiles)}")
# Using 9999 so that when printing this while debugging all the tiles would like up (Yeah I'm weird.)
# We're going to brute force filling in the grid, and we're going to do it inside out.
# So first things first pick a random corner tile and slap it in the upper right corner
# Then fill in the top edge, by plucking the first tile out of our edge bucket that shares an edge. and repeat.
# Then we'll fill in the left side, in the same manner.
# Then the remaining 2 sides.
# Filling in the center then just becomes a game of iterating through our center bucket until we find a tile that shares
# an exposed edge
grid = [[9999] * 12 for i in range(12)]
grid[0][0] = corner_tiles.popitem()[0]
# Fill in the top
for i in range(1, 11):
    grid[0][i] = next(edge for edge, neighbors in edge_tiles.items() if grid[0][i - 1] in neighbors and edge not in grid[0])
edge_tiles = {k: v for k, v in edge_tiles.items() if k not in grid[0]}
grid[0][11] = next(corner for corner, neighbors in corner_tiles.items() if grid[0][10] in neighbors and corner not in grid[0])
corner_tiles.pop(grid[0][11])

# Fill in the left
for j in range(1, 11):
    grid[j][0] = next(edge for edge, neighbors in edge_tiles.items() if grid[j - 1][0] in neighbors and edge not in {line[0] for line in grid})
grid[11][0] = next(corner for corner, neighbors in corner_tiles.items() if grid[10][0] in neighbors and corner not in {line[0] for line in grid})
corner_tiles.pop(grid[11][0])
edge_tiles = {k: v for k, v in edge_tiles.items() if k not in {line[0] for line in grid}}

# Fill in the right
for j in range(1, 11):
    grid[j][-1] = next(edge for edge, neighbors in edge_tiles.items() if grid[j - 1][-1] in neighbors and edge not in {line[-1] for line in grid})
grid[11][-1] = next(corner for corner, neighbors in corner_tiles.items() if grid[10][-1] in neighbors and corner not in {line[-1] for line in grid})
corner_tiles.pop(grid[11][-1])
edge_tiles = {k: v for k, v in edge_tiles.items() if k not in {line[-1] for line in grid}}

# Fill in the bottom
for i in range(1, 11):
    grid[-1][i] = next(edge for edge, neighbors in edge_tiles.items() if grid[-1][i - 1] in neighbors and edge not in grid[-1])
edge_tiles = {k: v for k, v in edge_tiles.items() if k not in grid[-1]}


def find_center_tile(x, y, debug=False):
    neighbors = set()
    for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        neighbor = grid[dy][dx]
        if neighbor != 9999:
            neighbors.add(neighbor)

    for idx, friends in center_tiles.items():
        if friends >= neighbors:
            return idx


# Fill in the rest!
for x, y in product(range(1, 11), repeat=2):
    if grid[y][x] != 9999:
        continue
    if (v := find_center_tile(x, y)) :
        grid[y][x] = v
        center_tiles.pop(v)


def print_grid(grid):
    for y, line in enumerate(grid):
        for i in range(10):
            print(" ".join(tiles[tile][i] for tile in line))
        print("")


# So begins the great aligning.
# First we want to align the top left corner piece with both of its neighbors.
# This will act as an anchor point for the rest of the puzzle.
# To do this, we first want to orient the neighbors such that their shaded edges exist in the find_all_edges(corner)
# results, then we can orient the corner so that the shared edges are aligned, and then flip the tiles as needed to make them actually match.
# Once those 3 are snapped in place, they can remain locked, and we align border tiles until we can lock them in place as well.
# Because of the way our grid came together, we only actually have to align 1 shared edge, and it should hook together properly with the
# the other edges.

corner = tiles[grid[0][0]]
right = tiles[grid[0][1]]
bottom = tiles[grid[1][0]]


for _ in range(4):
    if find_left(right) in find_all_edges(corner):
        break
    rotate(right)
else:
    flip_v(right)
    for _ in range(4):
        if find_left(right) in find_all_edges(corner):
            break
        rotate(right)

for _ in range(4):
    if find_right(corner) == find_left(right):
        break
    rotate(corner)
else:
    flip_v(corner)
    for _ in range(4):
        if find_right(corner) == find_left(right):
            break
        rotate(corner)

for _ in range(4):
    if find_top(bottom) in find_all_edges(corner):
        break
    rotate(bottom)
else:
    flip_h(bottom)
    for _ in range(4):
        if find_top(bottom) in find_all_edges(corner):
            break
        rotate(bottom)

if find_top(bottom) != find_bottom(corner):
    flip_h(bottom)
    if find_top(bottom) != find_bottom(corner):
        flip_v(corner)
        flip_v(right)
        if find_top(bottom) != find_bottom(corner):
            flip_h(bottom)
            if find_top(bottom) != find_bottom(corner):
                print("WHY GOD WHY")


def align_tile_to_left(tile, left):
    for _ in range(4):
        if find_left(tile) == find_right(left):
            break
        rotate(tile)
    else:
        flip_h(tile)
        for _ in range(4):
            if find_left(tile) == find_right(left):
                break
            rotate(tile)
    return find_left(tile) == find_right(left)


def align_tile_to_top(tile, top):
    for _ in range(4):
        if find_top(tile) == find_bottom(top):
            break
        rotate(tile)
    else:
        flip_h(tile)
        for _ in range(4):
            if find_top(tile) == find_bottom(top):
                break
            rotate(tile)
    return find_top(tile) == find_bottom(top)


# Corner is locked in, now we can do the left and top edges
for i in range(2, 12):
    left = tiles[grid[0][i - 1]]
    right = tiles[grid[0][i]]
    assert align_tile_to_left(right, left), (i, 0)

for j in range(2, 12):
    top = tiles[grid[j - 1][0]]
    bottom = tiles[grid[j][0]]
    assert align_tile_to_top(bottom, top), (0, j)

# With the top and left edges locked in, we can fill in the rest.
for x, y in product(range(1, 12), repeat=2):
    tile = tiles[grid[y][x - 0]]
    left = tiles[grid[y][x - 1]]
    assert align_tile_to_left(tile, left)

# WE HAVE A MAP! Now to remove the duplicate edges and search for some sea monsters.


def remove_edges_and_combine_grid(grid):
    corner = [""] * 96
    for j in range(0, 12):
        for i in range(0, 12):
            tile = [line[1:-1] for line in tiles[grid[j][i]][1:-1]]
            for idx, line in enumerate(tile):
                corner[idx + 8 * j] += line

    return corner


# Monster hunting time.
grid_map = remove_edges_and_combine_grid(grid)
monster = set()
monster_width = 20
monster_height = 3
for y, line in enumerate(open("monster.txt").read().split("\n")):
    for i, ch in enumerate(line):
        if ch == "#":
            monster.add((i, y))
# So the assumption was that once we can spot a whole monster, we don't need to keep spinning the map
# Because that answer worked when input, the assumption was correct!
monster_found = False
for _ in range(2):
    if monster_found:
        break
    flip_h(grid_map)
    for _ in range(4):
        if monster_found:
            break
        rotate(grid_map)
        for x in range(96 - monster_width):
            for y in range(96 - monster_height):
                if all(grid_map[y + my][x + mx] == "#" for mx, my in monster):
                    # Stop looking, we found a monster.
                    monster_found = True
                    for p in monster:
                        dx = x + p[0]
                        dy = y + p[1]
                        # Replace all the monster parts with O's so we can count the remaining # characters.
                        grid_map[dy] = grid_map[dy][:dx] + "O" + grid_map[dy][dx + 1 :]
print(f'Part 02: {sum(line.count("#") for line in grid_map)}')
