import re

vals = re.compile(r"\d+? [*+] \d+")
nums = re.compile(r"\(\d+?\)")
pzl = open("day_18.input").read().splitlines()
part_01 = []
for line in pzl:
    while (val := vals.findall(line)) :
        line = vals.sub(str(eval(val[0])), line, 1)
        while (num := nums.findall(line)) :
            line = nums.sub(str(eval(num[0])), line, 1)
    part_01.append(int(line))
print(sum(part_01))


adds = re.compile(r"\d+? \+ \d+")
groups = re.compile(r"\(([^)(]+)\)")


def search(expr):
    while group := groups.findall(expr):
        expr = groups.sub(search(group[0]), expr, 1)
    while add := adds.findall(expr):
        expr = adds.sub(str(eval(add[0])), expr, 1)

    return str(eval(expr))


print(sum(int(search(line)) for line in pzl))
