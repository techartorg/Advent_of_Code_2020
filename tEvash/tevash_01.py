# inputs = [
# 	1721,
# 	979,
# 	366,
# 	299,
# 	675,
# 	1456
# ]

# read in input and auto convert to int
with open("./inputs_1.txt") as f:
	inputs = [int(x) for x in f]

# part 1
def part1():
	for x in inputs:
		for y in inputs:
			if x + y == 2020:
				print(x * y)
				break

def part2():
	for x in inputs:
		for y in inputs:
			for z in inputs:
				if x + y + z == 2020:
					print(x * y * z)
					return


# peeked at bob's cause I'm no py wizard and had no idea this was a thing
# Decided that since it's a tuple, could just do without extra func since it's a small thing
from itertools import combinations
def part1_better():
	print(next(p[0] * p[1] for p in combinations(inputs, 2) if sum(p) == 2020))

def part2_better():
	print(next(p[0] * p[1] * p[2] for p in combinations(inputs, 3) if sum(p) == 2020))



# part1()
# part2()
# part1_better()
# part2_better()