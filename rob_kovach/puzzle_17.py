"""
Advent of Code - Day 17
"""

from copy import deepcopy, copy
from collections import defaultdict


input_ = '''.#.
..#
###
'''

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()


# Part 1 ----------------------------------------------------------------------
# Store the position and state of each cube as a dictionary.
# Unknown positions default to Inactive.
INITIAL_STATE = defaultdict(bool)
for y, i in enumerate([list(line) for line in input_.splitlines()]):
    for x, j in enumerate(i):
        INITIAL_STATE[(x, y, 0)] = j == '#'


def grow_space(cycle):
    """
    Adds empty cells around the data to prepare it for the next power cycle.
    
    """
    new_cycle = copy(cycle)
    for cube in cycle.keys():
        x, y, z = cube
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):
                for z1 in range(-1, 2):
                    if (x+x1, y+y1, z+z1) not in cycle:
                        new_cycle[(x+x1, y+y1, z+z1)] = False
    return new_cycle

def is_cube_active(position, cycle):
    return cycle[position]

def get_active_neighbor_count(position, cycle):
    activeNeighbors = 0
    for x1 in range(-1, 2):
        for y1 in range(-1, 2):
            for z1 in range(-1, 2):
                # Get off the offset position from our cube.
                newPosition = tuple(map(sum, zip(position, (x1, y1, z1))))
                # Don't count ourselves.
                if position == newPosition:
                    continue
                if is_cube_active(newPosition, cycle):
                    activeNeighbors += 1
    return activeNeighbors, cycle

def get_state(position, cycle):
    activeNeighbors, updatedCycle = get_active_neighbor_count(position, cycle)
    state = False
    if is_cube_active(position, updatedCycle):
        if activeNeighbors in [2, 3]:
            state = True
    else:
        if activeNeighbors == 3:
            state = True
    return state, updatedCycle

def boot_process():
    previous_round = grow_space(INITIAL_STATE)
    current_round = copy(previous_round)

    max_cycles = 6
    for i in range(max_cycles):
        cubes = list(previous_round.keys())
        for cube in cubes:
            active, previous_round = get_state(cube, previous_round)
            current_round[cube] = active
        
        previous_round = grow_space(current_round)

    return sum(state for state in current_round.values())


print(f'Part 1: {boot_process()}')

# Part 2 ----------------------------------------------------------------------
"""
Just a copy of part 1 with xyzw instead of xyz.
"""

CUBE_STATES = defaultdict(bool)

starting_condition = [list(line) for line in input_.splitlines()]

for y, i in enumerate(starting_condition):
    for x, j in enumerate(i):
        CUBE_STATES[(x, y, 0, 0)] = j == '#'

# add empty cells around the starting data
def grow_space(cycle):
    new_cycle = deepcopy(cycle)
    for cube in cycle.keys():
        x, y, z, w = cube
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):
                for z1 in range(-1, 2):
                    for w1 in range(-1, 2):
                        if (x+x1, y+y1, z+z1, w+w1) not in cycle:
                            new_cycle[(x+x1, y+y1, z+z1, w+w1)] = False
    return new_cycle

def is_cube_active(x, y, z, w, cycle):
    return cycle[(x, y, z, w)]

def get_active_neighbor_count(x, y, z, w, cycle):
    activeNeighbors = 0
    for x1 in range(-1, 2):
        for y1 in range(-1, 2):
            for z1 in range(-1, 2):
                for w1 in range(-1, 2):
                    # Don't count ourselves.
                    if (x, y, z, w) == (x+x1, y+y1, z+z1, w+w1):
                        continue
                    if is_cube_active(x+x1, y+y1, z+z1, w+w1, cycle):
                        activeNeighbors += 1
    return activeNeighbors, cycle

def get_state(x, y, z, w, cycle):
    activeNeighbors, updatedCycle = get_active_neighbor_count(x, y, z, w, cycle)
    state = False
    if is_cube_active(x, y, z, w, updatedCycle):
        if activeNeighbors in [2, 3]:
            state = True
    else:
        if activeNeighbors == 3:
            state = True
    return state, updatedCycle

def boot_process():

    previous_round = grow_space(deepcopy(CUBE_STATES))
    current_round = deepcopy(previous_round)

    max_cycles = 6
    for i in range(max_cycles):
        #print(len(previous_round.keys()))
        cubes = list(previous_round.keys())
        updatedCycle = deepcopy(previous_round)
        for cube in cubes:
            x, y, z, w = cube
            active, updatedCycle = get_state(x, y, z, w, updatedCycle)
            current_round[(x, y, z, w)] = active
        
        previous_round = grow_space(deepcopy(current_round))

    return sum(state for state in current_round.values())


#print(boot_process())