from collections import deque
from itertools import combinations, count
from typing import Deque

pzl = open("day_09.input").read().splitlines()

pzl_itr = map(int, pzl)

vals: Deque[int] = deque(maxlen=25)


def part_01():
    for val in map(int, pzl):
        if len(vals) != 25:
            vals.append(val)
            continue

        if val not in {a + b for a, b in combinations(vals, 2)}:
            return val

        vals.append(val)


val = part_01()
print(f"Part 01: {val}")


def part_02(val):
    for idx in count(2):
        window: Deque[int] = deque(maxlen=idx)
        for v in map(int, pzl):
            window.append(v)
            if sum(window) == val:
                return min(window) + max(window)


print(f"Part 02: {part_02(val)}")
