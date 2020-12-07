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


print(sum(contains_shiny_gold(bag) for bag in bag_map))

# need to add 1 to account for the actual bag itself.
def count_inner_bags(bag):
    return 1 + sum((count_inner_bags(inner_bag) * count) for count, inner_bag in bag_map[bag])


# Need to subtract 1 because we only care about bags inside our shiny gold bag, and we've accounted for it in the function.
# Stupid off by 1 issues will be he death of me.
print(count_inner_bags("shiny gold") - 1)
