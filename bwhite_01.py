import itertools
from operator import mul
from functools import reduce

vals = (
    1721,
    979,
    366,
    299,
    675,
    1456,
)
with open("day_01.input", "r") as f:
    vals = [int(v) for v in f]

print(next(mul(*p) for p in itertools.combinations(vals, 2) if sum(p) == 2020))
print(next(reduce(mul, p) for p in itertools.combinations(vals, 3) if sum(p) == 2020))