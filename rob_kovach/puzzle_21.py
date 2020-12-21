"""
Advent of Code: Day 21 - Allergen Assessment

--- Part 1 ---
You reach the train's last stop and the closest you can get to your vacation 
island without getting wet. There aren't even any boats here, but nothing 
can stop you now: you build a raft. You just need a few days' worth of food 
for your journey.

You don't speak the local language, so you can't read any ingredients lists. 
However, sometimes, allergens are listed in a language you do understand. 
You should be able to use this information to determine which ingredient 
contains which allergen and work out which foods are safe to take with you 
on your trip.

You start by compiling a list of foods (your puzzle input), one food per 
line. Each line includes that food's ingredients list followed by some or 
all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains 
zero or one allergen. Allergens aren't always marked; when they're listed 
(as in (contains nuts, shellfish) after an ingredients list), the 
ingredient that contains each listed allergen will be somewhere in the 
corresponding ingredients list. However, even if an allergen isn't listed, 
the ingredient that contains that allergen could still be present: maybe 
they forgot to label it, or maybe it was labeled in a language you 
don't know.

For example, consider the following list of foods:

    mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
    trh fvjkl sbzzf mxmxvkd (contains dairy)
    sqjhc fvjkl (contains soy)
    sqjhc mxmxvkd sbzzf (contains fish)


The first food in the list has four ingredients (written in a language you 
don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might 
contain other allergens, a few allergens the food definitely contains are 
listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain 
any of the allergens in any food in your list. In the above example, none 
of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. 
Counting the number of times any of these ingredients appear in any 
ingredients list produces 5: they all appear once each except sbzzf, which 
appears twice.

Determine which ingredients cannot possibly contain any of the allergens 
in your list. How many times do any of those ingredients appear?

--- Part 2 ---
Now that you've isolated the inert ingredients, you should have enough 
information to figure out which ingredient contains which allergen.

In the above example:

    mxmxvkd contains dairy.
    sqjhc contains fish.
    fvjkl contains soy.


Arrange the ingredients alphabetically by their allergen and separate 
them by commas to produce your canonical dangerous ingredient list. 
(There should not be any spaces in your canonical dangerous ingredient 
list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous 
ingredient list?

"""

from collections import defaultdict
from functools import reduce

LOCATION = __file__
INPUT_ = open(LOCATION.replace('.py', '_input.txt')).read()

# Create a Dictionary that stores the possible ingredients that
# may contain the allergen.
POSSIBILITIES = defaultdict(list)

# Store a master list of all ingredients (for Part 1).
# Don't remove duplicate entries!
ALL_INGREDIENTS = []

# Parse the input.
for x in INPUT_.splitlines():
    ingredients, allergens = x.split('(')
    ingredients = ingredients.strip()
    ingredients = ingredients.split(' ')
    ALL_INGREDIENTS.extend(ingredients)
    allergens = allergens.replace(')', '')
    allergens = allergens.replace('contains', '')
    allergens = allergens.split(',')
    allergens = [x.strip() for x in allergens]
    for a in allergens:
        POSSIBILITIES[a].append(ingredients)

# For each allergen, we know the possible list of ingredients per food.
# Find the common ingredients from each food for each allergen to exclude
# ingredients that are not common to all the foods.
REDUCED_POSSIBILITIES = {}
for allergen, ingredients in POSSIBILITIES.items():
    # Find the common set of possibilities amoung all foods.
    reduced = list(reduce(lambda i, j: i & j, (set(x) for x in ingredients)))
    REDUCED_POSSIBILITIES[allergen] = reduced

#print(REDUCED_POSSIBILITIES)

# Now that we have excluded all ingredients that couldn't contain
# the allergens, we know which ingredients to remove the list of
# all ingredients (for Part 1).
ALLERGENS = []
for x in REDUCED_POSSIBILITIES.values():
    ALLERGENS.extend(x)
ALLERGENS = list(set(ALLERGENS))
#print(ALLERGENS)

# Remove all the allergens from the master list of ingredients.
# Count the remaining ingredient for the answer to Part 1.
for item in ALL_INGREDIENTS[:]:
    if item in ALLERGENS:
        ALL_INGREDIENTS.remove(item)

print(f'Part 1 Answer: {len(ALL_INGREDIENTS)}')

# --- Part 2 ---
# Now that we know the possible ingredient that each allergen could be,
# we have to use a process of elimination to match each allergen to a 
# specific ingredient.

# Keep track of which allergens have been translated.
TRANSLATED = []
# Keep track of the allergen and its matched ingredient.
TRANSLATION = {}

while len(TRANSLATED) < len(REDUCED_POSSIBILITIES.keys()):

    # Loop over the dictionary of allergens, if they match just
    # one ingredient, remove that possibility from every other
    # allergen's list of potential ingredients.
    for allergen, ingredients in REDUCED_POSSIBILITIES.items():
        if allergen in TRANSLATED:
            continue

        if len(ingredients) == 1:
            match = ingredients[0]
            #print(f'{allergen} translates to {match}.')
            
            TRANSLATION[allergen] = match
            if not allergen in TRANSLATED:
                TRANSLATED.append(match)

    for allergen, ingredients in REDUCED_POSSIBILITIES.items():
        if allergen in TRANSLATED:
            continue
        for matched in TRANSLATION.values():
            if matched in ingredients:
                ingredients.remove(matched)

#print(TRANSLATED)
#print(TRANSLATION)

# To get the answer for Part 2 we have to sort the allergen 
# alphabetically, then joined the translated values together.
sorted_keys = sorted(TRANSLATION.keys())
answer = ','.join([TRANSLATION[x] for x in sorted_keys])

print(f'Part 2 Answer: {answer}')