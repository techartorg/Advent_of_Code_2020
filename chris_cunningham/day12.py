DIRECTIONS = {
    "N": 1j,
    "E": 1+0j,
    "S": 0-1j,
    "W": -1+0j
}

ROTATIONS = {
    "R90": -1j,
    "R180": -1,
    "R270": 1j,
    "L90": 1j,
    "L180": -1,
    "L270": -1j,
}


with open("inputs/day12.txt", 'r') as f:
    inputs = [(i[0], int(i[1:])) for i in f.read().splitlines()]

    def part_a():
        pos = 0j
        facing = 1+0j

        for inst, value in inputs:
            if inst == "F":
                pos += value * facing
            elif inst in ("L", "R"):
                facing *= ROTATIONS[f"{inst}{value}"]
            else:
                pos += DIRECTIONS[inst] * value

        return int(abs(pos.real) + abs(pos.imag))

    def part_b():
        waypoint = 10+1j
        pos = 0j

        for inst, value in inputs:
            if inst == "F":
                pos += value * waypoint
            elif inst in ("L", "R"):
                waypoint *= ROTATIONS[f"{inst}{value}"]
            else:
                waypoint += DIRECTIONS[inst] * value

        return int(abs(pos.real) + abs(pos.imag))

    print(f"part a: {part_a()}")
    print(f"part b: {part_b()}")
