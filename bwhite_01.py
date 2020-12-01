from itertools import combinations
from math import prod
from typing import List

vals: List[int] = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

with open("day_01.input", "r") as f:
    vals = [int(v) for v in f]

print(next(prod(p) for p in combinations(vals, 2) if sum(p) == 2020))
print(next(prod(p) for p in combinations(vals, 3) if sum(p) == 2020))
