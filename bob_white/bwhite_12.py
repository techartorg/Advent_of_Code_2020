pzl = """F10
N3
F7
R90
F11""".splitlines()

pzl = open("day_12.input").read().splitlines()

pos_01 = 0j
pos_02 = 0j
facing = 1 + 0j
waypoint = 10 + 1j

for mov in pzl:
    d = mov[0]
    v = int(mov[1:])
    if d == "F":
        pos_01 += v * facing
        pos_02 += v * waypoint
    elif d == "R":
        if v == 90:
            facing *= -1j
            waypoint *= -1j
        elif v == 270:
            facing *= 1j
            waypoint *= 1j
        elif v == 180:
            facing *= -1
            waypoint *= -1
    elif d == "L":
        if v == 90:
            facing *= 1j
            waypoint *= 1j
        if v == 270:
            facing *= -1j
            waypoint *= -1j
        if v == 180:
            facing *= -1
            waypoint *= -1
    elif d == "N":
        pos_01 += 1j * v
        waypoint += 1j * v
    elif d == "S":
        pos_01 -= 1j * v
        waypoint -= 1j * v
    elif d == "W":
        pos_01 -= v
        waypoint -= v
    elif d == "E":
        pos_01 += v
        waypoint += v

print(abs(pos_01.real) + abs(pos_01.imag))
print(abs(pos_02.real) + abs(pos_02.imag))
