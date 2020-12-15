pzl = list(map(int, open("day_15.input").read().split(",")))
# pzl = list(map(int, "0,3,6".split(",")))
# pzl = list(map(int, "2,1,3".split(",")))
# pzl = list(map(int, "1,3,2".split(",")))
from collections import defaultdict, deque
from typing import Dict, Deque

# pzl += [0] * (2020 - len(pzl))
pzl += [0] * (30000000 - len(pzl))

spoken: Dict[int, Deque[int]] = defaultdict(lambda: deque(maxlen=2))
for turn, num in enumerate(pzl):
    if not num and len((last_said := spoken[pzl[turn - 1]])) == 2:
        num = last_said[-1] - last_said[0]

    spoken[num].append(turn)
    pzl[turn] = num

print(f"Part 01: {pzl[2019]}")  # Off by ones will kill me.
print(f"Part 02: {pzl[-1]}")
