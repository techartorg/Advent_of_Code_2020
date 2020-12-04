import re


ex_input = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''
with open("inputs_4.txt", "r") as f:
	inputs = f.read()


def part1(inputs, fields):
	data = []
	last_data = {}
	for line in inputs.splitlines():
		if line == "":
			data.append(last_data)
			last_data = {}
			continue

		splits = line.split(" ")
		for sp in splits:
			key, value = sp.split(":")
			last_data[key] = value

	valid = [item for item in data if all(field in item.keys() for field in fields)]
	print(len(valid))
	return valid

def validate_data(last_data, fields):
	# do quick check to see if it can be valid at all
	if all(field in last_data.keys() for field in fields):
		for key, value in last_data.items():
			if key == "byr":
				valid_item = len(value) == 4 and (int(value) >= 1920 and int(value) <= 2002)
				# print(f"{valid_item}for byr")
			elif key == "iyr":
				valid_item = len(value) == 4 and (int(value) >= 2010 and int(value) <= 2020)
				# print(f"{valid_item}for iyr")
			elif key == "eyr":
				valid_item = len(value) == 4 and(int(value) >= 2020 and int(value) <= 2030)
				# print(f"{valid_item}for eyr")
			elif key == "hgt":
				if not any(measurement in value for measurement in ["cm", "in"]):
					valid_item = False
				if "cm" in value:
					num = int(value[:value.index("cm")])
					valid_item = num >= 150 and num <= 193
				elif "in" in value:
					num = int(value[:value.index("in")])
					valid_item =  num >= 59 and num <=76
				# print(f"{valid_item} for hgt {value}")
			elif key == "hcl":
				if not value.startswith("#") or len(value) > 7:
					valid_item = False
				else:
					valid_item = bool(re.compile(r'(\A#{1}[a-f0-9]{6})').search(value))
				# print(f"{valid_item} for hcl")
			elif key == "ecl":
			 	valid_item = any(clr in value for clr in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
			 	# print(f"{valid_item} for ecl")
			elif key == "pid":
				valid_item = len(value) == 9 and bool(re.compile(r'([0-9]{9})').search(value))
				# print(f"{valid_item} for pid")
			elif key == "cid":
				valid_item = True

			if not valid_item:
				# print(f"{key} : {value} failed")
				return False
	else:
		return False		
	return True

def part2(inputs, fields):
	last_data = {}
	valid = 0
	for line in inputs.splitlines():
		if line == "" and len(last_data.keys()):
			
			valid_data = validate_data(last_data, fields)
			# print(f"{valid_data} : {last_data}")
			if valid_data:
				valid += 1
				last_data = {}
				continue
			else:
				last_data = {}
			continue
		splits = line.split(" ")
		for sp in splits:
			key, value = sp.split(":")
			last_data[key] = value
	# print(f"validate final data: {last_data}: {validate_data(last_data, fields)}")
	if validate_data(last_data, fields):
		valid += 1
	print(valid)
	return valid

fields = [
	"byr",
	"iyr",
	"eyr",
	"hgt",
	"hcl",
	"ecl",
	"pid"
]
part1(inputs, fields)
part2(inputs, fields)
	