from math import prod
from collections import defaultdict
from ast import literal_eval
from typing import Dict, Set

# Notes doesn't have a heading, and is the first block, so we don't want to strip off the first line
notes, my_ticket, other_tickets = [block.splitlines()[1:] if idx else block.splitlines() for idx, block in enumerate(open("day_16.input").read().split("\n\n"))]

note_map: Dict[str, Set[int]] = defaultdict(set)
for note in notes:
    key, val = note.split(": ")
    for spread in val.split(" or "):
        min_, max_ = map(int, spread.split("-"))
        note_map[key].update(range(min_, max_ + 1))

tickets = [literal_eval(line) for line in other_tickets]
bad_tickets, errors = zip(*((idx, v) for idx, t in enumerate(tickets) for v in t if not any(v in vals for vals in note_map.values())))
print(f"Part 01: {sum(errors)}")

# Removing known bad tickets, also adding my hopefully valid ticket.
valid_tickets = [ticket for idx, ticket in enumerate(tickets) if idx not in bad_tickets]
valid_tickets.append(literal_eval(my_ticket[0]))

# find all fields that are valid for every column of ticket data.
potential_fields: Dict[str, Set[int]] = defaultdict(set)
for field, valid in note_map.items():
    for idx, column in enumerate(zip(*valid_tickets)):
        if all(c in valid for c in column):
            potential_fields[field].add(idx)

# Reduce the potential fields down to a single column index each.
# We sort them in by number of valid columns
# then strip already used columns from the rest of the fields
for potential, values in sorted(potential_fields.items(), key=lambda x: len(x[-1])):
    (current_field_index,) = values  # This will happily explode if we hit a column that still thinks more than one column is valid.
    for other_field, other_values in potential_fields.items():
        if potential == other_field:
            continue
        other_values.discard(current_field_index)

# Finally an answer! Also, remember my ticket is the last one in the list.
print(f"Part 02: {prod(valid_tickets[-1][idx.pop()] for field, idx in potential_fields.items() if field.startswith('departure'))}")
