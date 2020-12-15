"""
Advent of Code - Day 14
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read().splitlines()


def parse_input(data):
    """Parse the input into a dictionary."""

    # For each Mask, store a tuple of the memory address and value into
    # a dictionary.
    bitmasks = {}

    currentMask = None
    for line in input_:
        if line.startswith('mask'):
            mask = line.split('=', 1)[-1].strip()
            bitmasks[mask] = []
            currentMask = mask
        
        elif line.startswith('mem'):
            address, value = line.split('=', 1)
            addressInt = [x for x in list(address) if x.isdigit()]
            addressInt = int(''.join(addressInt))
            value = int(value.strip())
            bitmasks[currentMask].append((addressInt, value))

    return bitmasks


def int_to_binary(integer):
    """Convert an integer to a 36-bit binary representation."""
    return f'{integer:036b}'


def binary_to_int(value):
    """Convert binary number to an integer."""
    return int(value, 2)


def apply_bitmask(mask, value, currentValue):
    """Merges two binary numbers together using the bitmask."""

    value = int_to_binary(value)
    output = list(int_to_binary(currentValue))

    for i in range(len(mask)):
        if mask[i] == 'X':
            output[i] = value[i]
        else:
            output[i] = mask[i]
    value = ''.join(output)

    newValue = binary_to_int(value)
    return newValue


def part1():
    dataSet = parse_input(input_)
    # Track the computer's memory with a dictionary, where the
    # memory address is the key.
    memory = {}
    for mask, operations in dataSet.items():
        for op in operations:
            address = op[0]
            value = op[1]
            # Undefined memory addresses default to Zero.
            try:
                currentValue = memory[address]
            except:
                currentValue = 0

            newValue = apply_bitmask(mask, value, currentValue)
            memory[address] = newValue

    return sum(memory.values())


# Part 2 ----------------------------------------------------------------------

from itertools import product


def update_mask(mask, value):
    """Update "value" with bitmask "mask"."""

    output = list(int_to_binary(value))

    for i in range(len(mask)):
        if mask[i] == 'X':
            output[i] = 'X'
        if mask[i] == '1':
            output[i] = '1'
    
    output = ''.join(output)
    return output


def part2():
    dataSet = parse_input(input_)
    memory = {}
    for mask, operations in dataSet.items():
        for op in operations:
            address = op[0]
            value = op[1]

            newMask = update_mask(mask, address)
            # Get how many times "X" appears in the new Mask, generate
            # that many permutations of [0, 1].
            permutationCount = mask.count('X')
            permutations = product((0, 1), repeat=permutationCount)

            # for each permutation of [0, 1], fill in the "X" in
            # the bitmask. Convert the value to an Int and update
            # the memory address.
            for p in permutations:
                newMask = newMask.replace('X', r'{}')
                finalValue = newMask.format(*p)
                x = binary_to_int(finalValue)
                memory[x] = value
    
    return sum(memory.values())


if __name__ == '__main__':
    print(part1())
    print(part2())
