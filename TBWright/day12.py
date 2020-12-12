"""

"""

from math import pi, cos, sin

inputs = [(line[0], int(line[1:])) for line in open("inputs/day12_input.txt", "r").read().splitlines()]

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
RIGHT = 'R'
LEFT = 'L'
FORWARD = 'F'


def part01(input_list):
    x = y = 0
    direction = EAST
    for orient, amount in input_list:
        if orient == NORTH:
            y += amount
        elif orient == SOUTH:
            y -= amount
        elif orient == EAST:
            x += amount
        elif orient == WEST:
            x -= amount
        elif orient in [RIGHT, LEFT]:
            rots = amount // 90
            for i in range(rots):
                if direction == EAST:
                    direction = SOUTH if orient == RIGHT else NORTH
                elif direction == SOUTH:
                    direction = WEST if orient == RIGHT else EAST
                elif direction == WEST:
                    direction = NORTH if orient == RIGHT else SOUTH
                elif direction == NORTH:
                    direction = EAST if orient == RIGHT else WEST
        elif orient == FORWARD:
            if direction == EAST:
                x += amount
            elif direction == SOUTH:
                y -= amount
            elif direction == WEST:
                x -= amount
            elif direction == NORTH:
                y += amount
    return ((x, y), direction), abs(x) + abs(y)


def part02(input_list):
    x = y = 0
    wx = 10
    wy = 1
    for orient, amount in input_list:
        if orient == NORTH:
            wy += amount
        elif orient == SOUTH:
            wy -= amount
        elif orient == EAST:
            wx += amount
        elif orient == WEST:
            wx -= amount
        elif orient in [RIGHT, LEFT]:
            rots = amount // 90
            theta = -(pi/2) if orient == RIGHT else pi/2
            for i in range(rots):
                n_wx = int(round((wx * cos(theta)) - (wy * sin(theta))))
                n_wy = int(round((wx * sin(theta)) + (wy * cos(theta))))
                wx = n_wx
                wy = n_wy
        elif orient == FORWARD:
            x += wx*amount
            y += wy*amount
    return (x, y), abs(x) + abs(y)


print(part01(inputs))
print(part02(inputs))
