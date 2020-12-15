"""
Advent of Code - Day 15
"""

from collections import defaultdict

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read().split(',')

def solve(iterations):
    # keep track of the spoken numbers and on what 
    # turn they were spoken.
    numbers = [int(x) for x in input_]
    spoken_numbers = defaultdict(list)

    last_number_spoken = numbers[0]
    i = 0
    while i < iterations:
        # Seed the dictionary with the puzzle input.
        if i < len(numbers):
            n = numbers[i]
            last_number_spoken = n
            spoken_numbers[n].append(i+1)

        else:
            if last_number_spoken in spoken_numbers.keys():
                previous_turns_spoken = spoken_numbers[last_number_spoken]
                if len(previous_turns_spoken) == 1:
                    new_number = 0
                else:
                    new_number = previous_turns_spoken[-1] - previous_turns_spoken[-2]
                last_number_spoken = new_number
                spoken_numbers[new_number].append(i + 1)

        i += 1
    return last_number_spoken


if __name__ == '__main__':
    print(solve(2020))
    print(solve(30000000))