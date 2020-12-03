# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals

"""
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy,
it's certainly not safe: there's very minimal steering and the area is covered in trees.
You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. 

These aren't the only trees, though; due to something you read about once involving arboreal genetics and
biome stability, the same pattern repeats to the right many times.

You start on the open square (.) in the top-left corner and need to reach the bottom
(below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left
corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1.
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    
What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

# built-ins
from functools import reduce
# third-party

# first-party
from aoc import AdventUser, PuzzlePart

USER = AdventUser()


# puzzle logic
def skii_free(tree_map, slopes) -> int:
    trees = [sum(row[(x * c) % len(row)] == "#" for c, row in enumerate(tree_map[::y])) for x, y in slopes]
    return reduce((lambda x, y: x * y), trees)


# collect puzzle data
puzzle = USER.get_puzzle(3, 2020)
puzzle.input = puzzle.input.splitlines()

# answer submissions
puzzle.submit(skii_free(puzzle.input, [(3, 1)]), PuzzlePart.A)
puzzle.submit(skii_free(puzzle.input, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]), PuzzlePart.B)
