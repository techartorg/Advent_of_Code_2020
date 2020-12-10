from itertools import combinations, islice
from typing import Tuple, Iterator, Iterable


def window(seq: Iterable[int], n: int) -> Iterator[Tuple[int, ...]]:
    it = iter(seq)
    result = tuple(islice(it, n))

    if len(result) == n:
        yield result

        for elem in it:
            result = result[1:] + (elem,)
            yield result


def part_a() -> int:
    for i in window(inputs, preamble_len + 1):
        current = i[preamble_len]
        previous = i[:preamble_len]

        if not any(sum(x) == current for x in combinations(previous, 2)):
            return current


def part_b_old(target: int) -> int:
    for n in range(2, len(inputs)):
        for i in window(inputs, n):
            if sum(i) == target:
                return min(i) + max(i)


def part_b(target: int) -> int:
    high = 0
    low = 0
    running_sum = inputs[low]

    while running_sum != target:
        if running_sum < target:
            high += 1
            running_sum += inputs[high]
        elif running_sum > target:
            running_sum -= inputs[low]
            low += 1

    potential = inputs[low:high]
    return min(potential) + max(potential)


preamble_len = 25
with open("inputs/day09.txt", 'r') as f:
    inputs = [int(i) for i in f]

    invalid_num = part_a()
    print(f"part a: {invalid_num}")

    b = part_b(invalid_num)
    print(f"part b: {b}")
