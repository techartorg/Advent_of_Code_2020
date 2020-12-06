puzzle = open("day_06.input").read().split("\n\n")

from functools import reduce

print(sum(len(set(c for c in item if c not in "\n")) for item in puzzle))

print(sum(len(reduce(set.intersection, (set(line) for line in item.split("\n")))) for item in puzzle))
