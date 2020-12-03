import re

pzl_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split(
    "\n"
)

tst = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
v1 = 0
v2 = 0
with open("day_02.input", "r") as f:
    for line in f:
        if (m := tst.match(line)) :
            min_, max_, val, password = m.groups()
            v1 += int(min_) <= password.count(val) <= int(max_)
            v2 += (password[int(min_) - 1], password[int(max_) - 1]).count(val) == 1

print(v1)
print(v2)
# Not going to lie, I really love that doing this in a single comprehension is actually _more_ code then doing it in a loop.
# Fun experiment though
awful = list(
    map(
        sum,
        zip(
            *[
                (
                    int(min_) <= password.count(val) <= int(max_),
                    (password[int(min_) - 1], password[int(max_) - 1]).count(val) == 1,
                )
                for line in open("day_02.input", "r")
                # Imports in comprehensions?!
                if (reg := __import__("re"))
                if (match := reg.match(r"(\d+)-(\d+) (\w): (\w+)", line))
                # I've yet to find a better way of doing multiple unpacks in a comprehension expression.
                for min_, max_, val, password in (match.groups(),)
            ]
        ),
    )
)
print(awful)