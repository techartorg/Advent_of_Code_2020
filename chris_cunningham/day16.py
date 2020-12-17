from math import prod
from collections import defaultdict

Rules = defaultdict[str, set[int]]
Ticket = list[int]


def parse_notes(notes: str) -> Rules:
    notes_map: defaultdict[str, set[int]] = defaultdict(set)

    for note in notes.splitlines():
        key, values = note.split(": ", maxsplit=2)
        for v in values.split(" or "):
            start, end = (int(i) for i in v.split("-", maxsplit=2))
            notes_map[key] |= set(range(start, end + 1))

    return notes_map


def parse_input(input_str: str) -> tuple[Rules, Ticket, list[Ticket]]:
    notes, tickets = input_str.split("\nyour ticket:", maxsplit=2)
    notes = parse_notes(notes)
    your_ticket, nearby_tickets = tickets.split("\nnearby tickets:")
    your_ticket = [int(i) for i in your_ticket.split(",")]
    nearby_tickets = [[int(i) for i in t.split(",")] for t in nearby_tickets.strip().splitlines()]
    return notes, your_ticket, nearby_tickets


def filter_tickets(tickets: list[Ticket], rules: Rules) -> tuple[list[Ticket], int]:
    valid_tickets = []
    errors = 0

    for ticket in tickets:
        if all(any(val in rule for rule in rules.values()) for val in ticket):
            valid_tickets.append(ticket)
        else:
            errors += sum(val for val in ticket if not any(val in rule for rule in rules.values()))

    return valid_tickets, errors


with open("inputs/day16.txt", 'r') as f:
    def solve() -> tuple[int, int]:
        rules, my_ticket, nearby_tickets = parse_input(f.read())
        valid, errors = filter_tickets(nearby_tickets, rules)
        valid.append(my_ticket)

        possibilities: defaultdict[str, set[int]] = defaultdict(set)

        for field, rule in rules.items():
            for i, col in enumerate(zip(*valid)):
                if all(n in rule for n in col):
                    possibilities[field].add(i)

        sorted_possibilities = sorted(possibilities.items(), key=lambda x: len(x[-1]))

        for possible, values in sorted_possibilities:
            start_index, = values

            for other_field, other_values in sorted_possibilities:
                if possible == other_field:
                    continue
                other_values.discard(start_index)

        return errors, prod(my_ticket[idx.pop()] for field, idx in possibilities.items() if field.startswith("departure"))


    a, b = solve()
    print(f"part a: {a}")
    print(f"part b: {b}")
