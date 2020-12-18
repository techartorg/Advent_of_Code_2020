import re

vals = re.compile(r"\d+? [*+] \d+")
num = re.compile(r"\(\d+?\)")
pzl = open("day_18.input").read().splitlines()
part_01 = []
for line in pzl:
    while (f := vals.findall(line)) :
        line = vals.sub(str(eval(f[0])), line, 1)
        while (v := num.findall(line)) :
            line = num.sub(str(eval(v[0])), line, 1)
    part_01.append(int(line))
print(sum(part_01))


adds = re.compile(r"\d+? \+ \d+")
group = re.compile(r"\(([^)(]+)\)")


def search(expr):
    while grp := group.findall(expr):
        expr = group.sub(search(grp[0]), expr, 1)
    while ad := adds.findall(expr):
        expr = adds.sub(str(eval(ad[0])), expr, 1)

    return str(eval(expr))


print(sum(int(search(line)) for line in pzl))
