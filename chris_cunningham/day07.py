from typing import List, Tuple, Dict


def parse_rule(rule: str) -> Tuple[str, List[Tuple[int, str]]]:
    outer, contents = rule.split(" bags contain ")
    bags = [c.rsplit(maxsplit=1)[0].split(maxsplit=1) for c in contents.split(", ") if c != "no other bags."]
    bags = [(int(count), color) for count, color in bags]
    return outer, bags


with open("inputs/day07.txt", 'r') as f:
    rules: Dict[str, List[Tuple[int, str]]] = {k: v for k, v in (parse_rule(r) for r in f.read().splitlines())}

    def find_shiny_gold(start: str) -> bool:
        return start in rules and any(color == "shiny gold" or find_shiny_gold(color) for _, color in rules[start])

    def count_in_bag(start: str) -> int:
        return 1 + sum((count_in_bag(color) * count) for count, color in rules[start])

    part_a = sum(find_shiny_gold(bag) for bag in rules)
    print(f"part a: {part_a}")

    part_b = count_in_bag("shiny gold") - 1  # took me way to long to fix this off by 1
    print(f"part b: {part_b}")
