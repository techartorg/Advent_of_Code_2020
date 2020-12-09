with open("inputs/day05.txt", 'r') as f:
    ids = sorted(int(line.translate(str.maketrans("FLBR", "0011")), 2) for line in f.read().splitlines())
    print(f"part a: {ids[-1]}")
    missing = set(range(ids[0], ids[-1])).difference(ids).pop()
    print(f"part b: {missing}")
