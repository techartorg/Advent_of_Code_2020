pzl_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split(
    "\n"
)

pzl_input = open("day_02.input", "r").read().split("\n")

v1 = 0
v2 = 0
for line in pzl_input:
    rules, password = line.split(": ")
    min_max, val = rules.split()
    min_, max_ = map(int, min_max.split("-"))
    if min_ <= password.count(val) <= max_:
        v1 += 1
    if password[min_ - 1] == val and password[max_ - 1] == val:
        continue
    if password[min_ - 1] == val or password[max_ - 1] == val:
        v2 += 1

print(v1)
print(v2)
