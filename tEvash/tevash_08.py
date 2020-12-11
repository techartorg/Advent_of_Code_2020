with open("inputs_8.txt") as f:
	inputs = [x.strip().split(" ") for x in f.readlines()]

ex_inputs = [
	("nop","+0"),
	("acc","+1"),
	("jmp","+4"),
	("acc","+3"),
	("jmp","-3"),
	("acc","-99"),
	("acc","+1"),
	("jmp","-4"),
	("acc","+6")
]

def part1(inputs):
	ran_inst = []
	index = 0
	accumulator = 0
	while index not in ran_inst:
		inst = inputs[index]
		ran_inst.append(index)

		if inst[0] == "jmp":
			# print(f"jmp: {inst[1]} from {index}")
			index = index + int(inst[1])

		elif inst[0] == "nop":
			# print(f"nop: {index} : {index+1}")
			index += 1

		elif inst[0] == "acc":
			# print(f"acc: {accumulator} : {accumulator+ int(inst[1])}")
			accumulator += int(inst[1])
			index += 1

	return accumulator


def part2(inputs):
	ran_inst = []
	index = 0
	accumulator = 0

	while index not in ran_inst and index < len(inputs):
		inst = inputs[index]
		ran_inst.append(index)

		if inst[0] == "jmp":
			# print(f"jmp: {inst[1]} from {index}")
			new_ind = index + int(inst[1])
			if new_ind in ran_inst:
				ran_inst.remove(index)
				inputs[index] = ["nop", inst[1]]
			else:	
				index = index + int(inst[1])

		elif inst[0] == "nop":
			# print(f"nop: {index} : {index+1}")
			new_ind = index + 1
			if new_ind in ran_inst:
				ran_inst.remove(index)
				inputs[index] = ["jmp", inst[1]]
			else:	
				index += 1

		elif inst[0] == "acc":
			# print(f"acc: {accumulator} : {accumulator+ int(inst[1])}")
			accumulator += int(inst[1])
			index += 1

	return accumulator


print(f"Part1: {part1(inputs)}")
print(f"Part2: {part2(inputs)}")
