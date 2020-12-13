"""
Advent of Code - Day 12
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read().splitlines()

clockwise = ['N', 'E', 'S', 'W']
counterClockwise = ['N', 'W', 'S', 'E']

def change_direction(current_direction, direction, angle):
    steps = angle // 90
    if direction == 'L':
        compass = counterClockwise
    else:
        compass = clockwise
    new_dir = (compass.index(current_direction) + steps) % 4
    new_direction = compass[new_dir]
    return new_direction

def move_along_direction(direction, value, position):
    if direction == 'E':
        position[0] += value
    elif direction == 'W':
        position[0] -= value
    elif direction == 'N':
        position[1] += value
    elif direction == 'S':
        position[1] -= value
    return position

def part1():
    currentPosition = [0, 0]
    facing_dir = 'E'

    for dir_ in input_:
        instruction = dir_[0]
        value = int(dir_[1:])

        if instruction == 'F':
            currentPosition = move_along_direction(facing_dir, value, currentPosition)
        elif instruction in ['L', 'R']:
            facing_dir = change_direction(facing_dir, instruction, value)
        else:
            currentPosition = move_along_direction(instruction, value, currentPosition)

    return(abs(currentPosition[0]) + abs(currentPosition[1]))


# Part 2 ----------------------------------------------------------------------
def rotate_waypoint(waypoint, direction, angle):
    if direction == 'L':
        if angle == 90:
            waypoint = [-waypoint[1], waypoint[0]]
        if angle == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        if angle == 270:
            waypoint = [waypoint[1], -waypoint[0]]
    
    else:
        if angle == 90:
            waypoint = [waypoint[1], -waypoint[0]]
        if angle == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        if angle == 270:
            waypoint = [-waypoint[1], waypoint[0]]
    return waypoint

def move_to_waypoint(position, value, waypoint):
    position[0] += value * waypoint[0]
    position[1] += value * waypoint[1]
    return position


def move_waypoint(waypoint, direction, value):
    if direction == 'N':
        waypoint[1] += value
    elif direction == 'S':
        waypoint[1] -= value
    elif direction == 'E':
        waypoint[0] += value
    else:
        waypoint[0] -= value
    return waypoint
    

def part2():
    current_position = [0, 0]
    waypoint = [10, 1]

    for dir_ in input_:
        instruction = dir_[0]
        value = int(dir_[1:])

        if instruction == 'F':
            current_position = move_to_waypoint(current_position, value, waypoint)
        
        elif instruction in ['N', 'E', 'W', 'S']:
            waypoint = move_waypoint(waypoint, instruction, value)
        
        elif instruction in ['L', 'R']:
            waypoint = rotate_waypoint(waypoint, instruction, value)
    
    return(abs(current_position[0]) + abs(current_position[1]))

if __name__ == '__main__':
    print(part1())
    print(part2())