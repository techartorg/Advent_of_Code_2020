"""--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?


--- Part Two ---
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?"""

import string

def ParseValidPassports(passport_entries):
	required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid","cid")
	passports = []
	for p in passports_entries:
		keys = []
		values = []
		for pair in p:
			k, v = pair.split(":")
			keys.append(k)
			values.append(v)
		if set(keys)==set(required_fields) or ("cid" not in keys and len(keys)==7):
			passports.append(dict(zip(keys, values)))
	return passports

passports_entries = [row.split() for row in open('./input_04.txt', 'r').read().split("\n\n")]
valid_passports = ParseValidPassports(passports_entries)
print(f"Part 1 - How many passports are valid?\n{len(valid_passports)}\n")

""" ------------ PART 2 ------------ """

def validate_value_in_range(value, min_val, max_val):
	return value.isdigit() and int(value) in range(min_val,max_val+1)

def validate_height(value):
	if len(value)<3:
		return False
	if value[:-2].isdigit:
		height = int(value[:-2])
	else:
		return False
	if (value[-2:] == "cm" and height in range(150, 194)) or (value[-2:] == "in" and height in range(59, 77)):
		return True
	else:
		return False

def validate_hair_color(value):
	return value[0]=="#" and all(c in string.hexdigits for c in value[1:])

def validate_eye_color(value):
	return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validate_pid(value):
	return value.isdigit() and len(value)==9

def uber_validate_passports(passports):
	valid_passports=[]
	for p in passports:
		if(validate_value_in_range(p["byr"],1920,2002) and
			validate_value_in_range(p["iyr"],2010,2020) and
			validate_value_in_range(p["eyr"],2020,2030) and
			validate_height(p["hgt"]) and
			validate_hair_color(p["hcl"]) and
			validate_eye_color(p["ecl"]) and
			validate_pid(p["pid"])):
			valid_passports.append(p)
	return valid_passports

print(f"Part 2 - How many passports are valid with stricter rules?\n{len(uber_validate_passports(valid_passports))}\n")
