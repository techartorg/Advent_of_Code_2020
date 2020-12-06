with open("inputs/day06.txt", 'r') as f:
    groups = [[set(p) for p in grp.splitlines()] for grp in f.read().split("\n\n")]

    part_a = sum(len(set.union(*g)) for g in groups)
    print(f"part a: {part_a}")

    part_b = sum(len(set.intersection(*g)) for g in groups)
    print(f"part b: {part_b}")
