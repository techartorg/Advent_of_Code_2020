from collections import deque
from itertools import combinations
from typing import Deque

pzl = open("day_09.input").read().splitlines()


def part_01():
    window_sz = 25
    window: Deque[int] = deque(map(int, pzl[:window_sz]), maxlen=window_sz)
    for val in map(int, pzl[window_sz:]):
        if not any(a + b == val for a, b in combinations(window, 2)):
            return val

        window.append(val)


def part_02(val):
    for idx in range(2, len(pzl)):
        window: Deque[int] = deque(maxlen=idx)
        for v in map(int, pzl):
            window.append(v)
            if sum(window) == val:
                return min(window) + max(window)


print(f"Part 01: {(val := part_01())}")
print(f"Part 02: {part_02(val)}")
