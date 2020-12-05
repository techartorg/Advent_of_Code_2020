pzl = open("day_05.input").read().splitlines()
passes = []
for test in pzl:
    rows = range(128)
    columns = range(8)
    for val in test:
        if val == "F":
            rows = rows[: len(rows) // 2]
        elif val == "B":
            rows = rows[len(rows) // 2 :]
        if val == "R":
            columns = columns[len(columns) // 2 :]
        elif val == "L":
            columns = columns[: len(columns) // 2]
    passes.append(next(iter(rows)) * 8 + next(iter(columns)))

print(f"Part_01 {max(passes)}")

missing = set(passes).symmetric_difference(range(min(passes), max(passes)))
missing = {v for v in missing if v not in {min(passes), max(passes)}}
print(f"Part_02 {missing.pop()}")
