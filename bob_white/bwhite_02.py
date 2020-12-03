import re

pzl_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split(
    "\n"
)

pzl_input = open("day_02.input", "r").read().split("\n")
tst = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
v1 = 0
v2 = 0
for line in pzl_input:
    min_, max_, val, password = (
        m.groups() if (m := tst.match(line)) else ("-1", "-1", " ", "")
    )
    if int(min_) <= password.count(val) <= int(max_):
        v1 += 1
    if (password[int(min_) - 1], password[int(max_) - 1]).count(val) == 1:
        v2 += 1

print(v1)
print(v2)

awful = list(
    map(
        sum,
        zip(
            *[
                (
                    int(min_) <= password.count(val) <= int(max_),
                    (password[int(min_) - 1], password[int(max_) - 1]).count(val) == 1,
                )
                for line in open("day_02.input", "r").read().split("\n")
                if (reg := __import__("re"))
                if (match := reg.match(r"(\d+)-(\d+) (\w): (\w+)", line))
                for min_, max_, val, password in (match.groups(),)
            ]
        ),
    )
)
print(awful)