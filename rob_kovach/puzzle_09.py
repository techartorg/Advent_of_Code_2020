"""
Advent of Code - Day 9
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()

PREAMBLE_LENGTH = 25

input_ = [int(x) for x in input_.splitlines()]

def part1():
    invalidNumber = None
    i = 0
    while not invalidNumber:
        # gather all numbers after the preamble.
        number_set = input_[PREAMBLE_LENGTH:]

        for i in range(len(number_set)):
            # gather all numbers in the sliding window.
            window = input_[i:i+PREAMBLE_LENGTH]
            # the number to validate.
            number = input_[i+PREAMBLE_LENGTH]
            # store the successful numbers.
            pairs = []

            for j in window:
                diff = number - j

                # the number cannot be the sum of half its value.
                if diff == number / 2:
                    invalidNumber = number
                
                if diff in window:
                    pairs.append([j, diff])

            if not pairs:
                invalidNumber = number

            i += 1

    return invalidNumber

def part2():
    invalidNumber = part1()
    print(invalidNumber)

    range_ = []
    # Loop though numbers, collecting the sum of each number in the
    # list after the current number.
    for i, a in enumerate(input_):
        sum_ = a
        for j, b in enumerate(input_[i+1:]):
            sum_ += b
            if sum_ == invalidNumber:
                range_ = input_[i:i+j+2]
                break
    return min(range_) + max(range_)

if __name__ == '__main__':
    print(part2())