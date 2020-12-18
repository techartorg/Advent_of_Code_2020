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

# Messing with order of operations is silly and evil. But totally works.
# so basic idea for part 1, is get both __add__ and __mul__ on the same precident level.
# which means moving multiplcation to __sub__
class Part1(int):
    def __add__(self, b):
        return type(self)(self.real + b)

    def __sub__(self, b):
        return type(self)(self.real * b)


# Part 2 we basically want to swap the precident level
# which is pretty easy to do by swapping the operators
class Part2(int):
    def __mul__(self, b):
        return type(self)(self.real + b)

    def __add__(self, b):
        return type(self)(self.real * b)


digits = re.compile(r"(\d+)")
# same as the Part1 class above, swapping mul for sub
print(sum(eval(digits.sub(r"Part1(\1)", line.replace("*", "-"))) for line in pzl))
# Slighly longer song and dance to swap add and mul, but like the Part2 class, that is what we need to do here.
print(sum(eval(digits.sub(r"Part2(\1)", line.replace("*", "-").replace("+", "*").replace("-", "+"))) for line in pzl))