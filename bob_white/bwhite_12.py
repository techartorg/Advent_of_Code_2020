pzl = open("day_12.input").read().splitlines()

pos_01 = pos_02 = 0j
facing = 1 + 0j
waypoint = 10 + 1j

directions = {
    "N": 1j,
    "S": -1j,
    "E": 1,
    "W": -1,
}

rotations = {
    "R90": -1j,
    "R180": -1,
    "R270": 1j,
    "L90": 1j,
    "L180": -1,
    "L270": -1j,
}

for mov in pzl:
    direction = mov[0]
    distance = int(mov[1:])
    if direction == "F":
        pos_01 += distance * facing
        pos_02 += distance * waypoint
    elif mov in rotations:
        facing *= rotations[mov]
        waypoint *= rotations[mov]
    elif direction in directions:
        pos_01 += directions[direction] * distance
        waypoint += directions[direction] * distance


print(f"Part 01: {int(abs(pos_01.real) + abs(pos_01.imag))}")
print(f"Part 02: {int(abs(pos_02.real) + abs(pos_02.imag))}")
