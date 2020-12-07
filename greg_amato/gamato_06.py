# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals

"""
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane,
customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z.
All you need to do is identify the questions for which anyone in your group answers "yes".
Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier
and asks if you can help. For each of the people in their group, you write down the questions
for which they answer "yes", one per line. 

Another group asks for your help, then another, and eventually you've collected answers from every
group on the plane (your puzzle input). Each group's answers are separated by a blank line,
and within each group, each person's answers are on a single line.
For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes";
you need to identify the questions to which everyone answered "yes"!

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""

# built-ins
from functools import reduce
# third-party

# first-party
from aoc import AdventUser, PuzzlePart

USER = AdventUser()


# puzzle logic


# collect puzzle data
puzzle = USER.get_puzzle(6, 2020)
puzzle.input = puzzle.input_raw.split("\n\n")

a = sum(len(set(char for char in group if char not in "\n")) for group in puzzle.input)
b = sum(len(reduce(set.intersection, (set(passenger) for passenger in group.split("\n")))) for group in puzzle.input)

# answer submissions
puzzle.submit(a, PuzzlePart.A)
puzzle.submit(b, PuzzlePart.B)
