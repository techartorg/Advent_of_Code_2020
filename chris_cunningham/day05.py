with open("inputs/day05.txt", 'r') as f:
    ids = sorted(int(''.join('0' if c in "FL" else '1' for c in line.strip()), 2) for line in f)

    print(f"part a: {ids[-1]}")

    missing = set(range(ids[0], ids[-1])).difference(ids).pop()
    print(f"part b: {missing}")
