"""

"""

from lib.helpers import timer

INACTIVE = '.'
ACTIVE = '#'

infinite_grid = {(x, y, 0, 0): state for y, line in enumerate(open("inputs/day17_input.txt", "r").read().splitlines()) for x, state in enumerate(line)}


def get_neighbor_cube_coords(coord):
    xcoord, ycoord, zcoord, _ = coord
    neighbor_coords = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                neighbor_coord = (xcoord+x, ycoord+y, zcoord+z, 0)
                neighbor_coords.add(neighbor_coord)
    neighbor_coords.remove((xcoord, ycoord, zcoord, 0))
    return neighbor_coords


def get_neighbor_cube_coords_w(coord):
    xcoord, ycoord, zcoord, wcoord = coord
    neighbor_coords = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    neighbor_coord = (xcoord+x, ycoord+y, zcoord+z, wcoord+w)
                    neighbor_coords.add(neighbor_coord)
    neighbor_coords.remove((xcoord, ycoord, zcoord, wcoord))
    return neighbor_coords


def expand_grid(grid, iteration_to_expand_to):
    new_grid = grid.copy()
    x = y = 7 + iteration_to_expand_to
    for x_range in range(-iteration_to_expand_to, x+1):
        for y_range in range(-iteration_to_expand_to, y+1):
            for z_range in range(-iteration_to_expand_to, iteration_to_expand_to+1):
                if (x_range, y_range, z_range, 0) not in new_grid:
                    new_grid[(x_range, y_range, z_range, 0)] = INACTIVE
    return new_grid


def expand_grid_w(grid, iteration_to_expand_to):
    new_grid = grid.copy()
    x = y = 7 + iteration_to_expand_to
    for x_range in range(-iteration_to_expand_to, x+1):
        for y_range in range(-iteration_to_expand_to, y+1):
            for z_range in range(-iteration_to_expand_to, iteration_to_expand_to+1):
                for w_range in range(-iteration_to_expand_to, iteration_to_expand_to+1):
                    if (x_range, y_range, z_range, w_range) not in new_grid:
                        new_grid[(x_range, y_range, z_range, w_range)] = INACTIVE
    return new_grid


@timer
def solve(input_grid, cycles, use_w=False):
    itr = 0
    current_grid = input_grid.copy()

    while itr < cycles:
        current_grid = expand_grid(current_grid, itr+1) if not use_w else expand_grid_w(current_grid, itr+1)
        buffer_grid = current_grid.copy()
        for coord, state in current_grid.items():
            neighbor_coords = get_neighbor_cube_coords(coord) if not use_w else get_neighbor_cube_coords_w(coord)
            neighbor_states = [current_grid.get(coords, INACTIVE) for coords in neighbor_coords]
            if state == INACTIVE and neighbor_states.count(ACTIVE) == 3:
                buffer_grid[coord] = ACTIVE
            elif state == ACTIVE and neighbor_states.count(ACTIVE) not in [2, 3]:
                buffer_grid[coord] = INACTIVE
        current_grid = buffer_grid.copy()
        itr += 1
    return current_grid


part1_grid = solve(infinite_grid, 6)
print(list(part1_grid.values()).count(ACTIVE))

part2_grid = solve(infinite_grid, 6, use_w=True)
print(list(part2_grid.values()).count(ACTIVE))
