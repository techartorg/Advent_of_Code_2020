from typing import Tuple, List, Set

row_count = 128
col_count = 8


def parse_bsp(s: str) -> Tuple[int, int]:
    r = range(row_count)
    c = range(col_count)

    for char in s:
        if char == "F":
            r = r[:len(r) // 2]
        elif char == "B":
            r = r[len(r) // 2:]
        elif char == "R":
            c = c[len(c) // 2:]
        elif char == "L":
            c = c[:len(c) // 2]

    return r[0], c[0]


with open("inputs/day05.txt", 'r') as f:
    directions = [parse_bsp(i.strip()) for i in f]
    ids = sorted([r * 8 + c for r, c in directions])

    max_sid = max(ids)
    print(f"part a: {max_sid}")

    missing = set(range(ids[0], ids[-1])).difference(ids).pop()
    print(f"part b: {missing}")
