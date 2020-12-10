from collections import deque, defaultdict
from operator import sub
from typing import Dict

adapters = list(map(int, open("day_10.input").read().splitlines()))
device = max(adapters) + 3
adapters.append(device)
adapters.sort()


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
        # End of the tree, so return a 1
        if len(adapters) == 1:
            return 1
        # We can kill a branch early if the difference to the next node is over 3
        if abs(sub(*adapters[:2])) > 3:
            return 0
        # Branching paths, take the first 2, and test it against the rest of the nodes.
        # this basically spiderwebs us out into a whole lot of tests, hence why we need to use a lookup cache.
        a, b, *rest = adapters
        cache[k] = count_paths([a] + rest) + count_paths([b] + rest)
    return cache[k]


print(f"Part 02 {count_paths(adapters)}")
