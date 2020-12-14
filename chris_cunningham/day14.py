import re
from itertools import product, tee
from typing import Iterable

mem_re = re.compile(r"mem\[(\d+?)]")


def bits(n: int) -> Iterable[int]:
    while n:
        b = n & (~n+1)
        yield b
        n ^= b


def create_masks(mask_str: str) -> Iterable[int]:
    mask_len = mask_str.count("X")
    mask_str = mask_str.replace("X", "{}")

    mask_permutations = [i for i in product(("0", "1"), repeat=mask_len)]
    for p in mask_permutations:
        yield int(mask_str.format(*p), 2)


with open("inputs/day14.txt", 'r') as f:
    inputs = [i for i in f.read().splitlines()]

    def solve() -> tuple[int, int]:
        memory_a: dict[int, int] = {}
        memory_b: dict[int, int] = {}

        or_mask = 0x00
        and_mask = 0x00
        float_mask = 0
        floating_overrides: list[int] = []

        for line in inputs:
            loc, val = line.split(" = ", maxsplit=2)

            if m := mem_re.match(loc):
                loc, val = int(m.group(1)), int(val)
                memory_a[loc] = (val & and_mask) | or_mask
                for m in floating_overrides:
                    memory_b[(loc & (~float_mask)) | m] = val

            else:
                or_mask = int(val.replace("X", "0"), 2)
                and_mask = int(val.replace("X", "1"), 2)
                float_mask = int(val.replace("1", "0").replace("X", "1"), 2)
                floating_overrides = [*create_masks(val)]

        return sum(memory_a.values()), sum(memory_b.values())


    a, b = solve()
    print(f"part a: {a}")
    print(f"part b: {b}")
