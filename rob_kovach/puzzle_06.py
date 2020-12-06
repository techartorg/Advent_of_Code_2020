"""
Advent of Code Day 6
"""

location = __file__
groups = open(location.replace('.py', '_input.txt')).read().split('\n\n')

def get_answers(group):
    answers = 0
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in group:
            answers += 1
    return answers

def get_actual_answers(group):
    answers = 0
    individuals = group.splitlines()
    members = len(individuals)
    for i in 'abcdefghijklmnopqrstuvwxyz':
        count = 0
        for member in individuals:
            if i in member:
                count += 1
        if count == members:
            answers += 1
    return answers

def part1():
    return sum(get_answers(x) for x in groups)

def part2():
    return sum(get_actual_answers(x) for x in groups)

if __name__ == '__main__':
    print(part1())
    print(part2())