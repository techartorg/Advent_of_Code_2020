puzzle_input = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""[
    1:
].split(
    "\n\n"
)
fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
}
puzzle_input = open("day_04.input").read().split("\n\n")
# We can skip "cid" throughout, so we'll just not worry about it in our passport dictionaries.
passports = [{k: v for pair in group.split() for k, v in (pair.split(":"),) if k != "cid"} for group in puzzle_input]
# PART 01
print(sum(fields.symmetric_difference(passport) == {"cid"} for passport in passports))


# PART 02
valid = 0
for passport in passports:
    valid += bool(
        1920 <= int(passport.get("byr", "0")) <= 2002
        and 2010 <= int(passport.get("iyr", "0")) <= 2020
        and 2020 <= int(passport.get("eyr", "0")) <= 2030
        and ((hgt := passport.get("hgt", "")) and (hgt.endswith("cm") and 150 <= int(hgt[:-2]) <= 193) or (hgt.endswith("in") and 59 <= int(hgt[:-2]) <= 76))
        and ((hcl := passport.get("hcl", "")) and hcl.startswith("#") and len(hcl[1:]) == 6 and all(c in "abcdef1234567890" for c in hcl[1:]))
        and ((ecl := passport.get("ecl", "")) and ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
        and ((pid := passport.get("pid", "")) and len(pid) == 9 and all(c.isdigit() for c in pid))
    )


print(valid)