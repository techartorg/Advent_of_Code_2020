"""
Advent of Code - Day 9
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()

preambleLength = 25

input_ = [int(x) for x in input_.splitlines()]

def part1():
    invalidNumber = None
    valid = True
    i = 0
    while valid == True:
        for i in range(len(input_[preambleLength:])):
            number_set = input_[i:i+preambleLength]
            number = input_[i+preambleLength]
            pairs = []

            for j in number_set:
                diff = number - j
                if diff == number / 2:
                    invalidNumber = number
                    valid = False
                
                if diff in number_set:
                    pairs.append([j, diff])

            if not pairs:
                invalidNumber = number
                valid = False
            i += 1

    return invalidNumber


def part2():
    invalidNumber = part1()
    print(invalidNumber)

    range_ = None
    for i, number in enumerate(input_):
        sum_ = number
        for j, number2 in enumerate(input_[i+1:]):
            sum_ += number2
            if sum_ == invalidNumber:
                range_ = [i, i+j+2]
                break
    return min(input_[range_[0]:range_[1]]) + max(input_[range_[0]:range_[1]])


if __name__ == '__main__':
    print(part2())