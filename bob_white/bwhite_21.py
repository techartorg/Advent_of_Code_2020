from collections import defaultdict

pzl_input = open("day_21.input").read().splitlines()
# pzl_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

food_map = {frozenset(ingredients.split()): set(allergens[:-1].split(", ")) for line in pzl_input for ingredients, allergens in (line.split("(contains "),)}

all_ingredients = set.union(*map(set, food_map))
all_allergens = set.union(*food_map.values())

possible_allergens = set()
for allergen in all_allergens:
    possible_allergens.update(set.intersection(*(set(ingredients) for ingredients, allergens in food_map.items() if allergen in allergens)))

safe_ingredients = all_ingredients.difference(possible_allergens)
safe_count = defaultdict(int)
for ingredients, allergens in food_map.items():
    for ingredient in ingredients:
        if ingredient in safe_ingredients:
            safe_count[ingredient] += 1

print(f"Part 01: {sum(safe_count.values())}")
# At the outset each allergen could be associated with any of the triggers, which we found back in part 1
allergens_to_triggers = {allergen: possible_allergens.copy() for allergen in all_allergens}
# So we want to go through and do an intersection between all our allergens and the various ingredients that map back to that allergen.
for ingredients, allergens in food_map.items():
    for allergen in allergens:
        allergens_to_triggers[allergen].intersection_update(ingredients)

# Now we need to eliminate duplicates, this is a bit more complex than the train ticket alignment, and that's because of potential overlap.
# When I tried the old linear pass through I hit cases where there were still more than one trigger mapped to an allergen, so we need to allow
# for multiple passes.
while any(len(triggers) > 1 for triggers in allergens_to_triggers.values()):
    # Find all the triggers with a length of 1, we're going to remove them from the rest of the allergens
    found_triggers = set.union(*(triggers for triggers in allergens_to_triggers.values() if len(triggers) == 1))
    for allergen, triggers in allergens_to_triggers.items():
        if len(triggers) > 1:
            triggers.difference_update(found_triggers)
# We have to sort by ingredient, and then print out the allergens, which is why we sort on items and not values
print(f"Part 02: {','.join(triggers.pop() for _, triggers in sorted(allergens_to_triggers.items()))}")