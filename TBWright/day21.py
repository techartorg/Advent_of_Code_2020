"""

"""

from collections import defaultdict

dietary_dict = defaultdict(set)
occurences_count = defaultdict(int)

for line in open("inputs/day21_input.txt", "r").read().splitlines():
    ingredients, allergens = set(line[0:line.index('(')-1].split()), set(line[line.index('(')-1:].replace('(contains', '').replace(')', '').replace(',', '').split())
    for allergen in allergens:
        if allergen in dietary_dict:
            dietary_dict[allergen] = set(ingredient for ingredient in ingredients if ingredient in dietary_dict[allergen])
        else:
            dietary_dict[allergen] = ingredients
    for ingredient in ingredients:
        occurences_count[ingredient] += 1


def solve(foods_dict, count_dict):
    allergens_dict = foods_dict.copy()
    itr = 0
    for ingredient, count in count_dict.items():
        if all(ingredient not in food for food in allergens_dict.values()):
            itr += count
    used_ingredients = set()
    while any(len(allerg) > 1 for allerg in allergens_dict.values()):
        for allergen, ingredients in allergens_dict.items():
            if len(ingredients) == 1 and list(ingredients)[0] not in used_ingredients:
                used_ingredients.add(list(ingredients)[0])
            elif len(ingredients) > 1:
                for used_ingredient in used_ingredients:
                    if used_ingredient in ingredients:
                        allergens_dict[allergen].remove(used_ingredient)

    print(allergens_dict)
    return itr, ','.join(ingredient.pop() for allergen, ingredient in sorted(allergens_dict.items()))


count, allergen_ingredients = solve(dietary_dict, occurences_count)

print(count)
print(allergen_ingredients)
