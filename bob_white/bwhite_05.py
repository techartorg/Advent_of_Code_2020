pzl = open("day_05.input").read().splitlines()
passes = []
for boarding_pass in pzl:
    rows = range(128)
    columns = range(8)
    for val in boarding_pass:
        if val == "F":
            rows = rows[: len(rows) // 2]
        elif val == "B":
            rows = rows[len(rows) // 2 :]
        elif val == "L":
            columns = columns[: len(columns) // 2]
        elif val == "R":
            columns = columns[len(columns) // 2 :]
    v = rows[0] * 8 + columns[0]
    passes.append(v)

# New hotness!
# So the insight here is that because we're actually multiplying the row by 8 before adding,
# we're actually just creating a 10-bit number
passes = sorted(int("".join("0" if c in "FL" else "1" for c in boarding_pass), 2) for boarding_pass in pzl)

# So this is the same as above, but just adds the powers of 2 together. Reversing the boarding_pass string is because I can't get enumate to count down.
passes = sorted(sum(2 ** idx for idx, c in enumerate(boarding_pass[::-1]) if c in "BR") for boarding_pass in pzl)
print(f"Part_01 {passes[-1]}")

missing = set(range(passes[0], passes[-1])).difference(passes)
print(f"Part_02 {missing.pop()}")
