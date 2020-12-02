import re


inputs = []
with open("inputs_2.txt") as f:
	for line in f.readlines():
		inputs.append(line.strip().replace(":", ""))

def count_valid_passwords_1(inputs):
	valid = 0
	for line in inputs:
		# split based on - and " " (spaces)
		minimum, maximum, letter, password = re.split(r"[-\s]", line)
		if password.count(letter) < int(minimum) or password.count(letter) > int(maximum):
			continue
		valid += 1

	print(f"Part1: {valid}")


def count_valid_passwords_2(inputs):
	valid = 0
	for line in inputs:
		# split based on - and " " (spaces)
		start, end, letter, password = re.split(r"[-\s]", line)
		# tbf, I originally was just lazy and added a character to the start of the password 
		# <.< >.> It worked :P
		if ((password[int(start)-1] == letter and password[int(end)-1] != letter)
			or password[int(start)-1] != letter and password[int(end)-1] == letter):
			valid += 1

	print(f"Part2: {valid}")

count_valid_passwords_1(inputs)
count_valid_passwords_2(inputs)