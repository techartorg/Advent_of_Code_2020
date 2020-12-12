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
    elif (rot := rotations.get(mov)) :
        facing *= rot
        waypoint *= rot
    elif (direction_vector := directions.get(direction)) :
        pos_01 += direction_vector * distance
        waypoint += direction_vector * distance


print(f"Part 01: {int(abs(pos_01.real) + abs(pos_01.imag))}")
print(f"Part 02: {int(abs(pos_02.real) + abs(pos_02.imag))}")
