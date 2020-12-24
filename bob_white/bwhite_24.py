from pprint import pprint
from collections import defaultdict

instructions = open("day_24.input").read().splitlines()
# instructions = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew""".splitlines()

directions = {
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "e": (1, -1, 0),
}
grid = defaultdict(bool)
for line in instructions:
    moves = []
    while line:
        if line[0] in ("e", "w"):
            mov, *line = line
        else:
            mov = "".join(line[:2])
            line = line[2:]
        moves.append(directions[mov])
    coord = tuple(sum(x) for x in zip(*moves))
    grid[tuple(sum(x) for x in zip(*moves))] = not grid[tuple(sum(x) for x in zip(*moves))]
print(sum(grid.values()))

for _ in range(100):
    new_grid = defaultdict(bool)
    # not sure why I needed to inflate by 2, but I wasn't getting valid answers without it.
    # Probably some property of the weird coordinate system.
    x_range, y_range, z_range = [(min(x) - 2, max(x) + 2) for x in zip(*grid)]
    for x in range(*x_range):
        for y in range(*y_range):
            for z in range(*z_range):
                if x + y + z:
                    continue
                loc = (x, y, z)
                nearby = sum(grid[tuple(sum(x) for x in zip(loc, d))] for d in directions.values())
                if not grid[loc]:
                    new_grid[loc] = nearby == 2
                if grid[loc]:
                    new_grid[loc] = False if nearby == 0 or nearby > 2 else True
    grid = new_grid.copy()
    if _ % 10 == 9:
        print(_ + 1, sum(grid.values()))
print(sum(grid.values()))