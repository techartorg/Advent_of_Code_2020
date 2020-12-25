"""

"""

from collections import defaultdict
from lib.helpers import timer

valid_tiles = ['e', 'se', 'sw', 'w', 'nw', 'ne']
tiles_dict = {'e': (1, -1, 0), 'se': (0, -1, 1), 'sw': (-1, 0, 1), 'w': (-1, 1, 0), 'nw': (0, 1, -1), 'ne': (1, 0, -1)}

lines = [line for line in open("inputs/day24_input.txt", "r").read().splitlines()]


def tuple_add(a, b):
    return tuple([a[0]+b[0], a[1]+b[1], a[2]+b[2]])


def is_cell_valid(cell):
    return cell[0] + cell[1] + cell[2] == 0


# Use Regex, you dummy
def parse_input_line(line):
    direction_list = []
    itr = iter(line)
    while True:
        try:
            first_val = next(itr)
            if first_val in ('e', 'w'):
                direction_list.append(first_val)
            else:
                direction_list.append(first_val + next(itr))
        except StopIteration:
            break

    for ind, _dir in enumerate(direction_list):
        direction_list[ind] = tiles_dict[_dir]

    return direction_list


directions = [parse_input_line(line) for line in lines]


@timer
def part_01(direction_list):
    flipped = defaultdict(bool)
    for dir in direction_list:
        coord = (sum([val[0] for val in dir]), sum([val[1] for val in dir]), sum([val[2] for val in dir]))
        flipped[coord] = not flipped[coord]
    return flipped, sum(flip_val for coord, flip_val in flipped.items())


@timer
def part_02(coords_grid, iterations=100):
    itr = 0
    neighbor_cells = [(0, 1, -1), (0, -1, 1), (1, 0, -1), (-1, 0, 1), (-1, 1, 0), (1, -1, 0)]
    while itr < iterations:
        buffer_grid = coords_grid.copy()
        for cell, val in coords_grid.items():
            for neighbor in neighbor_cells:
                neighbor_cell = tuple_add(cell, neighbor)
                if not is_cell_valid(neighbor_cell):
                    continue
                if neighbor_cell not in coords_grid:
                    buffer_grid[neighbor_cell] = False
        coords_grid = buffer_grid.copy()
        for cell, val in coords_grid.items():
            neighbors = [neighbor_cell := tuple_add(cell, neighbor) for neighbor in neighbor_cells if is_cell_valid(neighbor_cell)]
            neighbor_sum = sum(coords_grid[neighbor] for neighbor in neighbors if neighbor in coords_grid)
            if val and (neighbor_sum == 0 or neighbor_sum > 2):
                buffer_grid[cell] = False
            elif not val and neighbor_sum == 2:
                buffer_grid[cell] = True

        coords_grid = buffer_grid.copy()
        itr += 1
    return sum(val for coord, val in coords_grid.items())


coords, black_tiles = part_01(directions[:])
print(black_tiles)
print(part_02(coords))
