import re

r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def part_a_test(matches: re.Match) -> bool:
    low, high, char, pw = matches.groups()
    return int(low) <= pw.count(char) <= int(high)


def part_b_test(matches: re.Match) -> bool:
    low, high, char, pw = matches.groups()
    c = (pw[int(low)-1] == char, pw[int(high)-1] == char)
    return sum(1 for i in c if i) == 1


with open("inputs/day02.txt", 'r') as f:
    data = [r.match(item) for item in f.readlines()]

    part_a = sum(1 for i in data if part_a_test(i))
    print(f"part_a: {part_a}")

    part_b = sum(1 for i in data if part_b_test(i))
    print(f"part_b: {part_b}")
