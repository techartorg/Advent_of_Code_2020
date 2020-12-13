from collections import Counter
from itertools import tee, islice
from typing import Iterator, Iterable, TypeVar

T = TypeVar('T')


def grouper(iterable: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    slices = (islice(it, i, None) for i, it in enumerate(tee(iterable, n)))
    return zip(*slices)


with open("inputs/day10.txt", 'r') as f:
    adapters = sorted(int(line) for line in f.read().splitlines())
    adapters.append(adapters[-1] + 3)  # pc

    def part_a() -> int:
        diffs = Counter(b - a for a, b in grouper(adapters, 2))
        diffs[adapters[0]] += 1  # wall
        return diffs[1] * diffs[3]

    def part_b() -> int:
        sums = 0
        paths = [0] * len(adapters)

        ptr = 0
        for i, jolts in enumerate(adapters):
            while ptr < i and adapters[ptr] < jolts-3:
                sums -= paths[ptr]
                ptr += 1

            paths[i] = sums + (jolts <= 3)
            sums += paths[i]

        return paths[-1]

    print(f"part a: {part_a()}")
    print(f"part b: {part_b()}")
