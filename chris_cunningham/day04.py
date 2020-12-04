from typing import Dict
import re

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
kvp_re = re.compile(r"(\S+):(\S+)")

hair_color_re = re.compile(r"^#[0-9a-f]{6}$")
height_re = re.compile(r"^(\d+)(cm|in)$")
eye_colors = {"amb", "blu",  "brn", "gry", "grn", "hzl", "oth"}
pid_re = re.compile(r"^\d{9}$")


def validate_range(v: int, low: int, high: int):
    return low <= v <= high


class Passport(object):
    def __init__(self, d: Dict[str, str]):
        self.base = d
        self.byr: int = int(i) if (i := d.get("byr")) else None
        self.iyr: int = int(i) if (i := d.get("iyr")) else None
        self.eyr: int = int(i) if (i := d.get("eyr")) else None
        self.hgt: str = d.get("hgt")
        self.hcl: str = d.get("hcl")
        self.ecl: str = d.get("ecl")
        self.pid: str = d.get("pid")
        self.cid: str = d.get("cid")

    def validate(self) -> bool:
        if self.byr is None or not 1920 <= self.byr <= 2002:
            return False

        if self.iyr is None or not 2010 <= self.iyr <= 2020:
            return False

        if self.eyr is None or not 2020 <= self.eyr <= 2030:
            return False

        if self.hgt is None:
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

        if self.hcl is None or hair_color_re.match(self.hcl) is None:
            return False

        if self.ecl is None or self.ecl not in eye_colors:
            return False

        if self.pid is None or pid_re.match(self.pid) is None:
            return False

        return True


with open("inputs/day04.txt", 'r') as f:
    passports = [{k: v for k, v in kvp_re.findall(i)} for i in f.read().split("\n\n")]

    part_a = sum(1 for i in passports if all(j in i for j in required_keys[:-1]))
    print(f"part a: {part_a}")

    part_b = sum(1 for i in passports if Passport(i).validate())
    print(f"part b: {part_b}")
