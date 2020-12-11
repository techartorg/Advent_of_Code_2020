from itertools import combinations

with open("inputs_9.txt") as f:
	inputs = [int(x) for x in f.readlines()]

ex_inputs = [
	35,
	20,
	15,
	25,
	47,
	40,
	62,
	55,
	65,
	95,
	102,
	117,
	150,
	182,
	127,
	219,
	299,
	277,
	309,
	576
]


def part1(inputs, pre_len = 25):
	index = pre_len
	while index < len(inputs):
		num = inputs[index]
		combos = [sum(x) for x in combinations(inputs[index-pre_len:index], 2)]
		# print(f"{num} :  {combos}")
		if num not in combos:
			return num
		index += 1


def part2(inputs):
	inv_num = part1(inputs)
	index = 0
	while True:
		summed = []
		for num in inputs[index:]:
			if sum(summed, num) == inv_num and len(summed) >= 2:
				summed.append(num)
				summed = sorted(summed)
				print(summed[0] + summed[len(summed) -1])
				return
			elif sum(summed, num) > inv_num:
				summed.clear()
				break
			summed.append(num)
		index += 1





print(part1(inputs))
part2(inputs)
