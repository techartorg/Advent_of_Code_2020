_TEST_DATA = """939
7,13,x,x,59,x,31,19"""

with open("inputs/day13.txt") as f:
    lines = f.read().splitlines()
    # lines = _TEST_DATA.splitlines()
    time = int(lines[0])
    bus_ids = [(i, int(bus)) for i, bus in enumerate(lines[1].split(",")) if bus != "x"]

    def part_a() -> int:
        closest = min(((i, abs(time % i - i)) for _, i in bus_ids), key=lambda x: x[1])
        return closest[0] * closest[1]

    def part_b() -> int:
        possible_sln = 0
        lcd = 1

        for offset, bus in bus_ids:
            while (possible_sln + offset) % bus != 0:
                possible_sln += lcd
            lcd *= bus

        return possible_sln


    print(f"part a: {part_a()}")
    print(f"part b: {part_b()}")
