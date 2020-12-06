# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals

"""

"""
# built-ins

# third-party

# first-party
from aoc import AdventUser, PuzzlePart

USER = AdventUser()

# globals
MEMBERS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
}


# puzzle logic
def valid_passports(data: list) -> int:
    return sum(MEMBERS.symmetric_difference(p) == {"cid"} for p in data)


def valid_passports_detailed(data: list) -> int:
    valid = 0
    for passport in data:
        hgt = passport.get("hgt", "")
        hcl = passport.get("hcl", "")
        ecl = passport.get("ecl", "")
        pid = passport.get("pid", "")
        if (
            1920 <= int(passport.get("byr", "0")) <= 2002
            and 2010 <= int(passport.get("iyr", "0")) <= 2020
            and 2020 <= int(passport.get("eyr", "0")) <= 2030
            and (hgt != "" and (hgt != "" and hgt.endswith("cm") and 150 <= int(hgt[:-2]) <= 193) or (hgt.endswith("in") and 59 <= int(hgt[:-2]) <= 76))
            and hcl != "" and hcl.startswith("#") and len(hcl[1:]) == 6 and all(char in "abcdef0123456789" for char in hcl[1:])
            and (ecl != "" and ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"})
            and (pid != "" and len(pid) == 9 and all(char.isdigit() for char in pid))
        ):
            valid += 1
    return valid


# collect puzzle data
puzzle = USER.get_puzzle(4, 2020)
puzzle.input_raw = puzzle.input_raw.split("\n\n")
puzzle.input = [{k: v for p in entry.split() for k, v in (p.split(":"),) if k != "cid"} for entry in puzzle.input_raw]

# answer submissions
puzzle.submit(valid_passports(puzzle.input), PuzzlePart.A)
puzzle.submit(valid_passports_detailed(puzzle.input), PuzzlePart.B)
