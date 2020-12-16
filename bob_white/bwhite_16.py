from operator import mul
from functools import reduce
from collections import defaultdict
from typing import Dict, Set


# I did not parse the notes out separately.
notes = """departure location: 26-404 or 427-951
departure station: 43-307 or 325-967
departure platform: 39-383 or 399-950
departure track: 31-157 or 178-969
departure date: 28-109 or 135-950
departure time: 38-622 or 631-958
arrival location: 35-61 or 69-957
arrival station: 36-216 or 241-951
arrival platform: 41-586 or 606-967
arrival track: 47-573 or 586-951
class: 31-439 or 445-957
duration: 35-925 or 939-965
price: 41-473 or 494-952
route: 45-742 or 754-963
row: 41-338 or 357-952
seat: 45-848 or 873-968
train: 37-183 or 197-952
type: 46-509 or 522-974
wagon: 32-69 or 81-967
zone: 37-759 or 780-967""".splitlines()


tickets = [list(map(int, line.split(","))) for line in open("day_16.input").read().splitlines()]


note_map: Dict[str, Set[int]] = defaultdict(set)
for note in notes:
    key, val = note.split(": ")
    for spread in val.split(" or "):
        m, x = map(int, spread.split("-"))
        note_map[key].update(range(m, x + 1))

errors = [(idx, v) for idx, t in enumerate(tickets) for v in t if not any(v in vals for vals in note_map.values())]
print(sum(v[1] for v in errors))
tickets = [ticket for idx, ticket in enumerate(tickets) if idx not in {v[0] for v in errors}]
# adding my ticket, hard coded style!
tickets.append([103, 197, 83, 101, 109, 181, 61, 157, 199, 137, 97, 179, 151, 89, 211, 59, 139, 149, 53, 107])

valid_index: Dict[str, Set[int]] = defaultdict(set)
for field, valid in note_map.items():
    for idx, column in enumerate(zip(*tickets)):
        if all(c in valid for c in column):
            valid_index[field].add(idx)

while not all(len(v) == 1 for v in valid_index.values()):
    found_fields = {field for field, idxes in valid_index.items() if len(idxes) == 1}
    for field in found_fields:
        idx_: int = valid_index[field].copy().pop()
        for values in valid_index.values():
            if len(values) == 1:
                continue
            values.discard(idx_)

print(reduce(mul, [tickets[-1][idx.pop()] for field, idx in valid_index.items() if field.startswith("departure")]))
