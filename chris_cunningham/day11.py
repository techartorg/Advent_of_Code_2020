from typing import Iterable

EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"

DIRECTIONS = [(-1-1j), (-1+0j), (-1+1j), -1j, 1j, (1-1j), (1+0j), (1+1j)]

with open("inputs/day11.txt", 'r') as f:
    input_grid = {x + y*1j: s for y, line in enumerate(f.read().splitlines()) for x, s in enumerate(line)}

    def get_adjacent(coord: complex, grid: dict[complex, str], *, skip_empty=False) -> Iterable[tuple[complex, str]]:
        for d in DIRECTIONS:
            delta = d + coord

            while skip_empty and grid.get(delta, None) is FLOOR:
                delta += d

            state = grid.get(delta, None)
            if state is None:
                continue

            yield delta, state


    def solve(num: int, skip_empty: bool) -> int:
        grid = input_grid.copy()

        while True:
            previous = grid.copy()

            for coord, state in grid.items():
                if state == EMPTY and all(s != OCCUPIED for _, s in get_adjacent(coord, previous, skip_empty=skip_empty)):
                    grid[coord] = OCCUPIED
                elif state == OCCUPIED and sum(i == OCCUPIED for _, i in get_adjacent(coord, previous, skip_empty=skip_empty)) >= num:
                    grid[coord] = EMPTY

            if grid == previous:
                break

        return sum(s == OCCUPIED for s in grid.values())

print(f"part a: {solve(4, False)}")
print(f"part b: {solve(5, True)}")

