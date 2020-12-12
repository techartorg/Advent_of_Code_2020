
with open("inputs_7.txt") as f:
	inputs = [x.strip() for x in f.readlines()]


ex_inputs= [
	"shiny gold bags contain 2 dark red bags.",
	"dark red bags contain 2 dark orange bags.",
	"dark orange bags contain 2 dark yellow bags.",
	"dark yellow bags contain 2 dark green bags.",
	"dark green bags contain 2 dark blue bags.",
	"dark blue bags contain 2 dark violet bags.",
	"dark violet bags contain no other bags."
]

def find_bags_containing_colour(roster, colour):
	bags = []
	for key, value in roster.items():
		if colour in (x[1] for x in value):
			bags.append(key)
			bags.extend(find_bags_containing_colour(roster, key))
	return bags

def part1(inputs):
	roster = {}
	for line in inputs:
		colour = line[:line.index(" bags")]
		contents = line.split("contain")[1].strip().replace(" bags", "").replace(" bag", "").split(", ")
		if "no other" in line:
			continue
		roster[colour] = []
		for content in contents:
			num = content[:content.index(" ")]
			content_colour = content[content.index(" ") + 1 :].strip(".")
			roster[colour].append((num, content_colour))

	bags = set(find_bags_containing_colour(roster, "shiny gold"))
	print(len(bags))


def count_bags(roster, colour):
	total = 1
	for bag in roster[colour]:
		if bag[1] == "None":
			print(f"No Bags in {colour}, return 1")
			return 1
		else:
			print(bag[0] * count_bags(roster, bag[1]))
			total += bag[0] * count_bags(roster, bag[1])
	print(total, colour)

	return total


def part2(inputs):
	roster = {}
	for line in inputs:
		colour = line[:line.index(" bags")]
		contents = line.split("contain")[1].strip().replace(" bags", "").replace(" bag", "").split(", ")
		roster[colour] = []
		for content in contents:
			if "no other" in line:
				num = 0
				content_colour = "None"
			else:
				num = int(content[:content.index(" ")])
				content_colour = content[content.index(" ") + 1 :].strip(".")

			roster[colour].append((int(num), content_colour))
	total = 0
	total = count_bags(roster,"shiny gold")
	print(f"Current Total: {total}")
	# minus the shiny gold bag from the count
	print(total - 1)

# part1(inputs)
# not 75,31
part2(inputs)