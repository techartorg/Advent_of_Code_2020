from collections import defaultdict

instructions = open("day_24.input").read().splitlines()

directions = {
    "e": 1,
    "w": -1,
    "ne": 1 - 1j,
    "nw": -1j,
    "se": 1j,
    "sw": -1 + 1j,
}

grid = defaultdict(int)
for line in instructions:
    # This is what happens when someone asks if you can one-line your janky text parsing.
    # Sadly the answer is yes! alos re.findall(line r'e|se|ne|w|sw|nw') should work.
    moves = (directions[m] for m in line.replace("sw", "sw ").replace("se", "se ").replace("ne", "ne ").replace("nw", "nw ").replace("w", "w ").replace("e", "e ").split())
    grid[sum(moves)] ^= 1

print(sum(grid.values()))

for _ in range(100):
    new_grid = grid.copy()
    # Adding in the surrounding tiles
    for tile in set(new_grid) | {tile + d for tile in new_grid for d in directions.values()}:
        nearby = sum(grid[tile + d] for d in directions.values())
        # Flipping the value based on the two rules.
        if (grid[tile] and (nearby == 0 or nearby > 2)) or (not grid[tile] and nearby == 2):
            new_grid[tile] ^= 1
    # Filtering out dead tiles, as it speeds up the process.
    grid = defaultdict(int) | {k: v for k, v in new_grid.items() if v}
print(sum(grid.values()))
