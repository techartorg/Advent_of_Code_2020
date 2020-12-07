"""
Advent of Code - Day 7
"""

location = __file__
baggage = open(location.replace('.py', '_input.txt')).read().splitlines()

# Dictionary of Bags where the string name is the key and the value is a Bag Object.
bags = {}

class Bag():
    def __init__(self, color):
        self.color = color
        # maintain a dictionary of the child bags and their count.
        self.children = {}
        self.parents = []

def collect_bags():
    """Pre-Populate the dictionary of bags with the color and their children.
    
    Mostly just string parsing...
    
    """
    for bag in baggage:
        color = bag.split(' contain')[0].split('bags')[0].strip()
        b = Bag(color)
        bags[color] = b

        children = bag.split(' contain ')[-1].split(',')
        for x in children:
            if 'no other' in x:
                continue
            child = x.split('bag')[0].strip()
            count = int(child[0])
            color2 = child[2:]
            b.children[color2] = count

def populate_bags():
    """Do a second pass on all the bags, recording their parent.
    
    More string parsing...
    
    """
    for bag in baggage:
        color = bag.split(' contain')[0].split('bags')[0].strip()
        c = bag.split(' contain ')[-1].split(',')
        for x in c:
            if 'no other' in x:
                continue
            b = x.split('bag')[0].strip()
            color2 = b[2:]
            bags[color2].parents.append(color)

def get_parents(bag):
    """Recurse through parents of the specified bag.

    The fun part!

    """
    parents = bags[bag].parents
    for parent in parents:
        grandparents = get_parents(parent)
        parents = list(set(parents + grandparents))
    return parents

def count_bags(bag):
    """
    Recurse through the contained bags to determine the total 
    number of bags within.
    
    """
    count = 0
    for child, num in bags[bag].children.items():
        count += num
        count += count_bags(child) * num
    return count

def part1():
    collect_bags()
    populate_bags()
    return len(get_parents('shiny gold'))

def part2():
    collect_bags()
    populate_bags()
    return count_bags('shiny gold')

if __name__ == '__main__':
    print(part1())
    print(part2())
