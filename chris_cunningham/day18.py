from pyparsing import infixNotation, oneOf, opAssoc, pyparsing_common, ParseResults

expression_strs = open("inputs/day18.txt", 'r').read().splitlines()

parser_a = infixNotation(pyparsing_common.integer, [(oneOf('* +'), 2, opAssoc.LEFT)])
parser_b = infixNotation(pyparsing_common.integer, [(oneOf('+'), 2, opAssoc.LEFT), (oneOf("*"), 2, opAssoc.LEFT)])


def apply(expression):
    result = 0
    op = "+"

    for i in expression:
        if isinstance(i, ParseResults):
            result = eval(f"{result}{op}{apply(i)}")
        elif isinstance(i, str):
            op = i
        else:
            result = eval(f"{result}{op}{i}")

    return result


print(f"part a: {sum(apply(i) for i in (parser_a.parseString(e) for e in expression_strs))}")
print(f"part b: {sum(apply(i) for i in (parser_b.parseString(e) for e in expression_strs))}")
