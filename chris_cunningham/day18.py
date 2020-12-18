from pyparsing import infixNotation, oneOf, opAssoc, pyparsing_common, ParseResults

expression_strs = open("inputs/day18.txt", 'r').read().splitlines()

parser_a = infixNotation(pyparsing_common.integer, [(oneOf('* +'), 2, opAssoc.LEFT)])
expressions_a = [parser_a.parseString(line) for line in expression_strs]

parser_b = infixNotation(pyparsing_common.integer, [(oneOf('+'), 2, opAssoc.LEFT), (oneOf("*"), 2, opAssoc.LEFT)])
expressions_b = [parser_b.parseString(line) for line in expression_strs]


def apply(expression):
    result = 0
    op = "+"

    for i in expression:
        if isinstance(i, ParseResults):
            result = eval(f"{result}{op}{apply(i)}")
        else:
            if isinstance(i, str):
                op = i
            else:
                result = eval(f"{result}{op}{i}")

    return result


print(f"part a: {sum(apply(i) for i in expressions_a)}")
print(f"part b: {sum(apply(i) for i in expressions_b)}")
