import re


def parse_inputs() -> tuple[dict[int, str], list[str]]:
    with open("inputs/day19.txt", 'r') as f:
        rules, data = f.read().split("\n\n", maxsplit=1)

        rules_dict = {}
        for i in rules.splitlines():
            key, rule = i.split(": ")
            rules_dict[int(key)] = rule

        data = data.splitlines()

    return rules_dict, data


def build_patterns(rules: dict[int, str], node: int, depth: int) -> str:
    if depth > 13:  # stops us from blowing the stack, started with a lower number then increased till the result became stable
        return ""

    result = "("

    for n in rules[node].split():
        if n == "|":
            result += n
        elif n.isdigit():
            result += build_patterns(rules, int(n), depth + 1)
        else:
            return n.replace('"', '')

    return result + ")"


def solve() -> tuple[int, int]:
    rules, data = parse_inputs()
    r = re.compile(build_patterns(rules, 0, 0))
    part_a = sum(1 for m in data if r.fullmatch(m))

    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    r = re.compile(build_patterns(rules, 0, 0))
    part_b = sum(1 for m in data if r.fullmatch(m))

    return part_a, part_b


a, b = solve()
print(f"part a: {a}")
print(f"part b: {b}")
