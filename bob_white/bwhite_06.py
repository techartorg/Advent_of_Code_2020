puzzle = open("day_06.input").read().split("\n\n")

from functools import reduce

print(sum(len(reduce(set.union, (set(person) for person in group.split("\n")))) for group in puzzle))
print(sum(len(reduce(set.intersection, (set(person) for person in group.split("\n")))) for group in puzzle))

# I like this version better, using unpacking instead of reduce.
print(sum(len(set.union(*(set(person) for person in group.splitlines()))) for group in puzzle))
print(sum(len(set.intersection(*(set(person) for person in group.splitlines()))) for group in puzzle))