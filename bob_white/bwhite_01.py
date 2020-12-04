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

answers = [
    next(
        prod(p)
        for p in combinations(map(int, open("day_01.input").readlines()), i)
        if sum(p) == 2020
    )
    for i in (2, 3)
]
print(f"Part 1: {answers[0]} \nPart 2: {answers[1]}")
