rules = open("day_07.input").read().splitlines()

bag_map = {}
for rule in rules:
    outer, *_, inner = rule.partition(" bags contain ")
    bag_map[outer] = inner


valid_bags = {"shiny gold"}
all_bags = list(bag_map)
valid_count = len(valid_bags)

while True:
    for bag in all_bags:
        if any(b in bag_map[bag] for b in valid_bags):
            valid_bags.add(bag)
    all_bags = [bag for bag in all_bags if bag not in valid_bags]
    if len(valid_bags) == valid_count:
        print(len(valid_bags) - 1)
        break
    valid_count = len(valid_bags)


def count_inner_bags(bag):
    if "no other" in bag_map[bag]:
        return 1
    c = 1
    for contains in bag_map[bag].split(", "):
        count, *name, _ = contains.split()
        name = " ".join(name)
        c += int(count) * count_inner_bags(name)
    return c


print(count_inner_bags("shiny gold") - 1)
