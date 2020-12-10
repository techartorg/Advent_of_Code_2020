"""

"""

from itertools import tee
from time import perf_counter
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ret = func(*args, **kwargs)
        print(f"{func.__name__.replace('_', ' ')} took: {perf_counter() - start:.8f} seconds")
        return ret
    return wrapper


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


input_list = sorted([int(line) for line in open("inputs/day10_input.txt", "r").read().splitlines()])
input_list.append(max(input_list)+3)


@timer
def part01():
    diff = [input_list[0] - 0]
    for first, second in pairwise(input_list):
        diff.append(second - first)
    return diff.count(1) * diff.count(3)


@timer
def part02():
    ptr = 0
    chunk_sum = 0
    valid_paths = [0] * len(input_list)

    for ind, digit in enumerate(input_list):
        while ptr < ind and input_list[ptr] < digit-3:
            chunk_sum -= valid_paths[ptr]
            ptr += 1

        valid_paths[ind] = chunk_sum + (digit <= 3)
        chunk_sum += valid_paths[ind]

    return int(valid_paths[-1]), valid_paths


print(part01())
print(part02())
