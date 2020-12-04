from typing import Dict
import re

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
kvp_re = re.compile(r"(\S+):(\S+)")

hair_color_re = re.compile(r"^#[0-9a-f]{6}$")
height_re = re.compile(r"^(\d+)(cm|in)$")
eye_colors = {"amb", "blu",  "brn", "gry", "grn", "hzl", "oth"}
pid_re = re.compile(r"^\d{9}$")


class Passport(object):
    def __init__(self, d: Dict[str, str]):
        self.byr = int(d.get("byr", 0))
        self.iyr = int(d.get("iyr", 0))
        self.eyr = int(d.get("eyr", 0))
        self.hgt = d.get("hgt", "")
        self.hcl = d.get("hcl", "")
        self.ecl = d.get("ecl", "")
        self.pid = d.get("pid", "")
        self.cid = d.get("cid", "")

    def validate(self) -> bool:
        if not 1920 <= self.byr <= 2002:
            return False

        if not 2010 <= self.iyr <= 2020:
            return False

        if not 2020 <= self.eyr <= 2030:
            return False

        if m := height_re.match(self.hgt):
            n, unit = m.groups()
            n = int(n)
            if unit == "cm" and not 150 <= n <= 193:
                return False
            elif unit == "in" and not 59 <= n <= 76:
                return False
        else:
            return False

        if hair_color_re.match(self.hcl) is None:
            return False

        if self.ecl not in eye_colors:
            return False

        if pid_re.match(self.pid) is None:
            return False

        return True


with open("inputs/day04.txt", 'r') as f:
    passports = [{k: v for k, v in kvp_re.findall(i)} for i in f.read().split("\n\n")]

    part_a = sum(1 for i in passports if all(j in i for j in required_keys[:-1]))
    print(f"part a: {part_a}")

    part_b = sum(1 for i in passports if Passport(i).validate())
    print(f"part b: {part_b}")
