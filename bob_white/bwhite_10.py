from collections import deque, defaultdict
from operator import sub
from typing import Dict

adapters = sorted(map(int, open("day_10.input").read().splitlines()))
device = max(adapters) + 3
adapters.append(device)


jitter_counter: Dict[int, int] = defaultdict(int)
pair = deque([0], maxlen=2)
for val in adapters:
    pair.append(val)
    jitter_counter[abs(sub(*pair))] += 1
print(f"Part 01 {jitter_counter[1] * jitter_counter[3]}")

cache = {}


def count_paths(adapters) -> int:
    k = tuple(adapters)
    if k not in cache:
        # Branching paths, take the first 2 items, and test it against the rest of the nodes.
        # this basically spiderwebs us out into a whole lot of tests, hence why we need to use a lookup cache.
        # We do out early if there is a gap greater than 3 between the next two numbers, this is a dead branch.
        try:
            a, b, *rest = adapters
        except ValueError:
            return 1
        else:
            if b - a > 3:
                return 0
            cache[k] = count_paths([a] + rest) + count_paths([b] + rest)
    return cache[k]


print(f"Part 02 {count_paths(adapters)}")
