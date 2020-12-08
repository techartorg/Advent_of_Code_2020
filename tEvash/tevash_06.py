
with open("inputs_6.txt") as f:
	inputs = f.read().split("\n\n")


def part1(inputs):
	count = 0
	for ans in inputs:
		count += len(set(ans.replace("\n", "")))

	print(count)

def part2(inputs):
	count = 0
	for ans in inputs:
		# get unique characters
		uniques = set(ans.replace("\n", ""))
		# then loop and count if each line (\n split)
		# has the character in it. If not, don't count it
		for char in uniques:
			char_count = 0
			for line in ans.split("\n"):
				if char in line:
					char_count += 1
			if char_count == len(ans.split("\n")):
				count += 1
	print(count)

part1(inputs)
part2(inputs)