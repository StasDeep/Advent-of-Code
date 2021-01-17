import re
from collections import Counter

from utils import read, p1, p2


def main():
    # Parse and count ingredients and allergens
    full_list = [
        (match.group(1).split(), match.group(2).split(", ")) for line in read()
        if (match := re.search(r"(.*) \(contains (.*)\)", line))
    ]
    full_ingreds = sum([item[0] for item in full_list], start=[])
    full_allergs = sum([item[1] for item in full_list], start=[])
    allergs_count = Counter(full_allergs)
    ingreds_count = Counter(full_ingreds)

    # Find the ingredients that can have allergens
    possible_allergs_for_ingreds = {}
    for ingred in set(full_ingreds):
        not_allergs = set(sum([item[1] for item in full_list if ingred not in item[0]], start=[]))
        possible_allergs = set(full_allergs) - not_allergs
        if possible_allergs:
            possible_allergs_for_ingreds[ingred] = possible_allergs

    # Part 1 answer is the total count of non-allergen ingredients
    p1(sum(ingreds_count[i] for i in set(full_ingreds) if i not in possible_allergs_for_ingreds))

    # Match ingredients to allergens by looking for ingredients with only one possible allergen option
    allergen_map = {}
    while len(allergen_map) != len(allergs_count):
        for ingred in set([i for i in possible_allergs_for_ingreds if i not in allergen_map]):
            possible_allergs = set(a for a in possible_allergs_for_ingreds[ingred] if a not in allergen_map.values())
            if len(possible_allergs) == 1:
                allergen_map[ingred] = possible_allergs.pop()

    # Part 2 answer is the list of ingredients sorted by the associated allergens
    p2(",".join(sorted(allergen_map.keys(), key=lambda i: allergen_map[i])))
