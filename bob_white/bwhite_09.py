from collections import deque
from itertools import combinations, count
from typing import Deque

pzl = open("day_09.input").read().splitlines()


def part_01():
    preamble_length = 25
    vals: Deque[int] = deque(maxlen=preamble_length)
    for val in map(int, pzl):
        if len(vals) != preamble_length:
            vals.append(val)
            continue

        if val not in {a + b for a, b in combinations(vals, 2)}:
            return val

        vals.append(val)


print(f"Part 01: {(val := part_01())}")


def part_02(val):
    for idx in count(2):
        window: Deque[int] = deque(maxlen=idx)
        for v in map(int, pzl):
            window.append(v)
            if sum(window) == val:
                return min(window) + max(window)


print(f"Part 02: {part_02(val)}")
