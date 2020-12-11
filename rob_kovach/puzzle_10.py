"""
Advent of Code - Day 10
"""

location = __file__
input_ = open(location.replace('.py', '_input.txt')).read()

ADAPTERS = [int(x) for x in input_.splitlines()]
ADAPTERS = sorted(ADAPTERS)

def part1():
    voltage = 0
    diff1 = 0
    diff2 = 0
    diff3 = 1
    i = 0
    while i < len(ADAPTERS):
        diff = ADAPTERS[i] - voltage
        if diff == 1:
            diff1 += 1
        elif diff == 2:
            diff2 += 1
        elif diff == 3:
            diff3 += 1
        voltage = ADAPTERS[i]
        i += 1
    return diff1 * diff3


ADAPTERS.insert(0, 0)
# Store the number of times each adapter can reach the end.
# Huge thanks to Bob for patiently explaining how to leverage
# the cache.
cache = {}

def walk_compatible_adapters(adapter):
    """
    Recurses from the adapter to the end of the chain,
    recording how many times it reached the end.
    """
    if adapter not in cache:
        compatible_adapters = []
        # Count the number of times we reach the end with this
        # adapter.
        count = 0
        if adapter == ADAPTERS[-1]:
            count += 1
        else:
            # Get the compatible adapters. Because of the voltage rules,
            # the compatible adapters will always be within the next 3 items.
            index = ADAPTERS.index(adapter)
            diff = 0
            i = 1
            while diff <= 3:
                try:
                    diff = ADAPTERS[index+i] - adapter
                except IndexError:
                    break
                if diff <= 3:
                    compatible_adapters.append(ADAPTERS[index+i])
                i += 1
        for a in compatible_adapters:
            count += walk_compatible_adapters(a)
        cache[adapter] = count
    return cache[adapter]


if __name__ == '__main__':
    print(part1())
    print(get_compatible_adapters(ADAPTERS[0]))