import time
from collections import defaultdict
from typing import List, Tuple, Dict

rules = open("day_07.input").read().splitlines()
bag_map: Dict[str, List[Tuple[int, str]]] = defaultdict(list)
for rule in rules:
    outer, *_, contents = rule.partition(" bags contain ")
    if "no other" not in contents:
        for c in contents.split(", "):
            contains = c.split()
            bag_map[outer].append((int(contains[0]), " ".join(contains[1:-1])))

# This initial contains check here is needed, because otherwise the bag_size changes during iteration because its a defaultdict
def contains_shiny_gold(bag):
    return bag in bag_map and any(color == "shiny gold" or contains_shiny_gold(color) for _count, color in bag_map[bag])


start = time.time()
print(sum(contains_shiny_gold(bag) for bag in bag_map))
print(time.time() - start)

# need to add 1 to account for the actual bag itself.
def count_inner_bags(bag):
    return 1 + sum((count_inner_bags(inner_bag) * count) for count, inner_bag in bag_map[bag])


# Need to subtract 1 because we only care about bags inside our shiny gold bag, and we've accounted for it in the function.
# Stupid off by 1 issues will be he death of me.
print(count_inner_bags("shiny gold") - 1)

# Really surprised by how much faster this runs. Probably all the function calls in the recursive version.
def iterative_part1():
    valid_bags = {"shiny gold"}
    while True:
        old_valid = valid_bags.copy()
        for bag, contents in bag_map.items():
            if bag in valid_bags:
                continue
            for _cnt, color in contents:
                if color in valid_bags:
                    valid_bags.add(bag)
                    break

        if len(old_valid) == len(valid_bags):
            break
    # Off by one again, need to account for the fact that we start with 'shiny gold'
    # in the initial set.
    print(len(valid_bags) - 1)


start = time.time()
iterative_part1()
print(time.time() - start)
