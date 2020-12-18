"""

"""

eq_list = [line for line in open("inputs/day18_input.txt", "r").read().splitlines()]


def solve_equation(substring, part_2=False):
    ss = substring.split(' ')
    while True:
        if len(ss) == 1:
            break
        if ss.count('+') and part_2:
            if ss.count('+') > 0:
                first_plus_ind = ss.index('+')
                eq = ''.join(ss[first_plus_ind - 1:first_plus_ind + 2])
                solve = [str(eval(eq))]
                ss = ' '.join(ss[:first_plus_ind - 1] + solve + ss[first_plus_ind + 2:]).split(' ')
        else:
            eq = ''.join(ss[:3])
            solve = [str(eval(eq))]
            ss = solve + ss[3:]
    return ss[0]


def solve_equations(equation_list, part_2=False):
    itr = 0
    for equation in equation_list:
        while '(' in equation:
            last_open_ind = equation.rfind('(')
            next_closed_ind = equation.find(')', last_open_ind)
            paren_eq = equation[last_open_ind+1:next_closed_ind]
            paren_solve = solve_equation(paren_eq, part_2=part_2)
            equation = equation.replace(equation[last_open_ind:next_closed_ind+1], paren_solve)
        itr += int(solve_equation(equation, part_2=part_2))
    return itr


print(solve_equations(eq_list))
print(solve_equations(eq_list, part_2=True))