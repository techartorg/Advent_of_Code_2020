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
    passes.append(rows[0] * 8 + columns[0])

print(f"Part_01 {max(passes)}")

missing = set(range(min(passes), max(passes))).difference(passes)
print(f"Part_02 {missing.pop()}")
