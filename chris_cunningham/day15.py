from array import array

inputs = [int(i) for i in r"15,12,0,14,3,1".split(",")]
iter_count_a = 2020
iter_count_b = 30_000_000


def solve() -> tuple[int, int]:
    last = inputs[-1]
    seen = array('I', [0]) * iter_count_b
    for i, v in enumerate(inputs, 1):
        seen[v] = i

    a = -1
    for i in range(len(inputs), iter_count_b):
        j = seen[last]
        seen[last] = i

        if i == iter_count_a:
            a = last

        last = 0 if j == 0 else i - j

    return a, last


part_a, part_b = solve()
print(f"part a: {part_a}")
print(f"part b: {part_b}")
