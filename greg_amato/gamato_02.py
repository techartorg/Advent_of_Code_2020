# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals

"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport;
the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by
the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords
(according to the corrupted database) and the corporate policy when that password was set.
"""
# built-ins

# third-party

# first-party
from aoc import AdventUser, PuzzlePart

USER = AdventUser()


# puzzle logic
def get_valid_pass(input_seq):
    valid = 0
    for policy_pass in input_seq:
        policy, pwd = policy_pass.split(': ')
        count, char = policy.split(' ')
        low, high = [int(x) - 1 for x in count.split('-')]

        if int(low) <= pwd.count(char) <= int(high):
            valid += 1

    return valid


def get_valid_pass_indexed(input_seq):
    valid = 0
    for policy_pass in input_seq:
        policy, pwd = policy_pass.split(': ')
        count, char = policy.split(' ')
        low, high = [int(x) - 1 for x in count.split('-')]

        if not(pwd[low] == char and pwd[high] == char) and (pwd[low] == char or pwd[high] == char):
            valid += 1

    return valid


# collect puzzle data
puzzle = USER.get_puzzle(2, 2020)
puzzle_input = [x for x in puzzle.input.splitlines()]

# answer submissions
puzzle.submit(get_valid_pass(puzzle_input), PuzzlePart.A)
puzzle.submit(get_valid_pass_indexed(puzzle_input), PuzzlePart.B)
