"""
Advent of Code - Day 18
"""

import re


location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()


def calculate(string):
    """Parses the numbers from left to right, applying the
    operators from left to right."""
    digits = []
    operators = []
    for token in string.split(' '):
        if token.isnumeric():
            digits.append(int(token))
        elif token in ['+', '*']:
            operators.append(token)

    # Initialize the return value as the first operation.
    # Then update the value for each additional operator.
    if operators[0] == '*':
        value = digits[0] * digits[1]
    else:
        value = digits[0] + digits[1]
    
    for i, op in enumerate(operators):
        if i == 0:
            continue
        if op == '*':
            value *= digits[i+1]
        else:
            value += digits[i+1]
    
    return value


def eval_expression(formula):
    exp = formula
    while '(' in exp:
        # extract the inner group of operators, solve, and update the expression.
        result = re.search("\(([0-9+* ]+)\)", exp)
        substring = result.group(1)
        evaluated = calculate(substring)
        exp = exp.replace(f'({substring})', str(evaluated), 1)
    return calculate(exp)


# Part 1 Solution
print(sum(eval_expression(x) for x in input_.splitlines()))


# Part 2 ----------------------------------------------------------------------
def calculate2(formula):
    """Apply Addition Before Multiplication."""
    exp = formula

    # Resolve each Addition Operation and update the Expression.
    while '+' in exp:
        result = re.search("(\d+[ ]\+[ ]\d+)", exp)
        substring = result.group(1)
        value = eval(substring)
        exp = exp.replace(f'{substring}', str(value), 1)
    
    # after resolving all the additions, we can multiply all
    # the remaining numbers together.
    exp = exp.replace('*', ' ')
    x = 1
    numbers = [int(x) for x in exp.split()]
    for n in numbers:
        x *= n
    return x


def eval_expression2(formula):
    exp = formula
    while '(' in exp:
        # extract the inner group of operators.
        result = re.search("\(([0-9+* ]+)\)", exp)
        substring = result.group(1)
        evaluated = calculate2(substring)
        exp = exp.replace(f'({substring})', str(evaluated), 1)
    return calculate2(exp)

# Part 2 solve
print(sum(eval_expression2(x) for x in input_.splitlines()))
