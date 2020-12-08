# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals

"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have
time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and
their contents; bags must be color-coded and must contain specific quantities of other color-coded bags.
Apparently, nobody responsible for these regulations considered how long they would take to enforce!

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty,
every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag
colors would be valid for the outermost bag?

How many bag colors can eventually contain at least one shiny gold bag? 

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the
ridiculous number of bags you need to buy!

Of course, the actual rules have a small chance of going several levels deeper than this example;
be sure to count all of the bags, even if the nesting becomes topologically impractical!

How many individual bags are required inside your single shiny gold bag?
"""

# built-ins

# third-party

# first-party
from aoc import AdventUser, PuzzlePart

USER = AdventUser()


# puzzle logic
def contained_bag_counter(rule_list, bag_type: str) -> list:
    bags = []
    for rule in rule_list:
        bag = rule.find(" bags contain")
        if bag_type in rule[bag:]:
            bags.append(rule[:bag])
            bags.extend(contained_bag_counter(rule_list, rule[:bag]))
    return bags


def get_containing_bags_count(bag_data, bag_type: str) -> int:
    bags = {b[0].strip(): b[1].strip().split(" , ") for b in [b.replace("bags", "").replace("bag", "").strip(".").split("contain") for b in bag_data]}

    def get_bag(bag):
        total = 1
        if "no other" in bags[bag]:
            return 1
        for colorway in bags[bag]:
            total += int(colorway.split()[0]) * get_bag(" ".join(colorway.split()[1:]))
        return total

    return get_bag(bag_type)


# collect puzzle data
puzzle = USER.get_puzzle(7, 2020)

# answer submissions
puzzle.submit(len(set(contained_bag_counter(puzzle.input_raw.splitlines(), "shiny gold"))), PuzzlePart.A)
puzzle.submit(get_containing_bags_count(puzzle.input_raw.splitlines(), "shiny gold") - 1, PuzzlePart.B)
