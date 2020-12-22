"""

"""

from lib.helpers import timer

inputs = open("inputs/day19_input.txt", "r").read().splitlines()
rules = {_input.split(':', 1)[0]: _input.split(':', 1)[1].lstrip(' ').replace('"', '') for _input in inputs[:inputs.index('')]}
codes = inputs[inputs.index('')+1:]


def parse_rule(rule_dict, rule_ind, code):
    rule = rule_dict[rule_ind]
    print(rule)

    if not rule[0].isnumeric():
        if not code:
            return []
        if code[0] == rule[0]:
            return [code[1:]]
        return []

    code_matches = []
    for subrule in rule.split('|'):
        possible_code_matches = [code]
        for rule_part in subrule.split():
            possible_code_matches = [new_match for match in possible_code_matches for new_match in parse_rule(rule_dict, rule_part, match)]
            print(possible_code_matches)
            if not possible_code_matches:
                break
        code_matches += possible_code_matches
    return code_matches


@timer
def part_01():
    return sum(1 for code in codes if '' in parse_rule(rules, '0', code))


@timer
def part_02():
    new_rules = rules.copy()
    new_rules['8'] = '42 | 42 8'
    new_rules['11'] = '42 31 | 42 11 31'
    return sum(1 for code in codes if '' in parse_rule(new_rules, '0', code))


print(part_01())
# print(part_02())
