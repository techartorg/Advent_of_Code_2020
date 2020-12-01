from itertools import combinations
from operator import mul
from functools import reduce
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


def prod(*args) -> int:
    return reduce(mul, args)


print(next(prod(*p) for p in combinations(vals, 2) if sum(p) == 2020))
print(next(prod(*p) for p in combinations(vals, 3) if sum(p) == 2020))
