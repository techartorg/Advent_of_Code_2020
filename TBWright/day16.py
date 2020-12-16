"""

"""

from collections import defaultdict
from math import prod
from lib.helpers import timer


def make_ranges_from_string(input_str):
    first_range, second_range = input_str.split(': ')[1].split(' or ')
    output_list = []
    for _range in [first_range, second_range]:
        minrange, maxrange = _range.split('-')
        output_list.append(range(int(minrange), int(maxrange)+1))
    return output_list


def make_ranges_from_input(input_str_block):
    ranges_dict = {}
    for line in input_str_block:
        ranges_dict[line.split(':')[0]] = make_ranges_from_string(line)
    return ranges_dict


def make_total_range_set(ranges):
    total_range = set()
    for _range in ranges:
        total_range.update(set(_range))
    return total_range


input_file = open("inputs/day16_input.txt", "r")
ranges_list = make_ranges_from_input([next(input_file).strip() for x in range(20)])
next(input_file)
next(input_file)
my_ticket = [int(val) for val in next(input_file).split(',')]
next(input_file)
next(input_file)
nearby_tickets = [[int(val) for val in line.split(',')] for line in input_file.read().splitlines()]


@timer
def part01(input_ranges, input_nearby_tickets):
    invalid_num_sum = 0
    invalid_tickets = set()
    total_input_ranges = set()
    for ranges in input_ranges.values():
        for range_val in ranges:
            range_set = set(range_val)
            total_input_ranges.update(range_set)
    for ind, ticket in enumerate(input_nearby_tickets):
        for val in ticket:
            if val not in total_input_ranges:
                invalid_tickets.add(ind)
                invalid_num_sum += val

    return invalid_num_sum, invalid_tickets


@timer
def part02(input_ranges, invalid_tickets, input_nearby_tickets, input_my_ticket):
    index_lists = defaultdict(list)
    for ind, ticket in enumerate(input_nearby_tickets):
        if ind in invalid_tickets:
            continue
        for ind1, val in enumerate(ticket):
            index_lists[ind1].append(val)

    pairings = defaultdict(int)
    possibilities = list(input_ranges.keys())
    invalid_sets = defaultdict(set)
    while len(possibilities) > 0:
        for ind, val_list in index_lists.items():
            if len(possibilities) == 1:
                pairings[possibilities.pop(0)] = ind
                break
            invalid_descs = set()
            for desc, ranges in input_ranges.items():
                tot_range = make_total_range_set(ranges)
                for val in val_list:
                    if val not in tot_range:
                        invalid_descs.add(desc)
                        break
            invalid_sets[ind] = set(possibilities).difference(invalid_descs)
            if len(invalid_sets[ind]) == 1:
                pairing_name = invalid_sets[ind].pop()
                pairings[pairing_name] = ind
                possibilities.remove(pairing_name)

    return prod([val for ind, val in enumerate(input_my_ticket) if ind in [pairings[name] for name in pairings.keys() if 'departure' in name]])


total_invalid_sum, invalid_ticket_inds = part01(ranges_list, nearby_tickets)
product_of_departures = part02(ranges_list, invalid_ticket_inds, nearby_tickets, my_ticket)


print(total_invalid_sum)
print(product_of_departures)
