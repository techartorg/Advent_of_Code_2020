from math import prod
from itertools import count, islice, cycle

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

# Keeping with my tradition of crafting horrible list comprehension based solutions
# Rob Kovach used the really nice insight of ::dy to iterate through the list and not need an infite loop, much smarter
print(prod(sum(line[(dx * c) % len(line)] == "#" for c, line in enumerate(trees[::dy])) for dx, dy in ((3, 1),)))
print(prod(sum(line[(dx * c) % len(line)] == "#" for c, line in enumerate(trees[::dy])) for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))


def nth(itr, idx):
    return next(islice(itr, idx, idx + 1))


# This one uses cycle to loop instead of % mathing it
print(prod(sum(nth(cycle(line), dx * c) == "#" for c, line in enumerate(trees[::dy])) for dx, dy in ((3, 1),)))
print(prod(sum(nth(cycle(line), dx * c) == "#" for c, line in enumerate(trees[::dy])) for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
