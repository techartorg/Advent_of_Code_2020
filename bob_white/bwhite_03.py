from math import prod
from itertools import count

trees = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""[
    1:
].splitlines()


trees = [line.strip() for line in open("day_03.input")]


def count_trees_on_slope(dx: int, dy: int) -> int:
    tree_count = 0
    for c in count(1):
        try:
            if trees[dy * c][(dx * c) % len(trees[0])] == "#":
                tree_count += 1
        except IndexError:
            break
    return tree_count


print(count_trees_on_slope(3, 1))
print(prod(count_trees_on_slope(dx, dy) for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
