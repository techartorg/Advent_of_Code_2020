"""
Advent of Code - Day 7
"""

""" Test Input
baggage = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''
"""

location = __file__
baggage = open(location.replace('.py', '_input.txt')).read().splitlines()

bags = {}

def collect_bags():
    """
    Pre-Populate the dictionary of bags with the color.
    """
    for bag in baggage:
        color = bag.split(' contain')[0].split('bags')[0].strip()
        c = bag.split(' contain ')[-1].split(',')
        bags[color] = []

def populate_bags():
    """
    Do a second pass on all the bag colors, recording who their parent is.
    """
    for bag in baggage:
        color = bag.split(' contain')[0].split('bags')[0].strip()
        c = bag.split(' contain ')[-1].split(',')
        for x in c:
            if 'no other' in x:
                continue
            b = x.split('bag')[0].strip()
            color2 = b[2:]
            bags[color2].append(color)

def get_parents(bag):
    """
    Recurse through parents of the specified bag.
    """
    parents = bags[bag]
    for parent in parents:
        grandparents = get_parents(parent)
        parents = list(set(parents + grandparents))
    return parents

def part1():
    collect_bags()
    populate_bags()
    return len(get_parents('shiny gold'))

if __name__ == '__main__':
    print(part1())

