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


def get_count(adapter):
    if adapter not in cache:
        cache[adapter] = sum(get_count(ad) for ad in tree[adapter]) or 1  # end point,
    return cache[adapter]


adapters.insert(0, 0)
tree = {ad: [a for a in adapters if a > ad and a - ad <= 3] for ad in adapters}
print(f"part_02 {get_count(0)}")
