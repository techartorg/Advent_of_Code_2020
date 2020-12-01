# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals

"""
-- Day 1: Report Repair --

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture
of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left
over from a past vacation. They offer you a second one if you can find three numbers in your
expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

# built-ins
from functools import reduce
from itertools import combinations
# third-party

# first-party
from aoc import AdventUser, PuzzlePart

USER = AdventUser()


# puzzle logic
def find_report_entries(inputs, length: int = 2):
    for i in range(len(inputs)):
        for j in combinations(inputs, i):
            if len(j) == length and sum(j) == 2020:
                return reduce((lambda x, y: x * y), j)


# collect puzzle data
puzzle = USER.get_puzzle(1, 2020)
puzzle_input = [int(x) for x in puzzle.input.splitlines()]

# answer submissions
puzzle.submit(find_report_entries(puzzle_input), PuzzlePart.A)
puzzle.submit(find_report_entries(puzzle_input, 3), PuzzlePart.B)
