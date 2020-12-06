puzzle = open("day_06.input").read().split("\n\n")

from functools import reduce

print(sum(len(set(c for c in group if c not in "\n")) for group in puzzle))

print(sum(len(reduce(set.intersection, (set(person) for person in group.split("\n")))) for group in puzzle))
