from functools import lru_cache

from utils import read, p1, p2


class Bag:

    def __init__(self, color):
        self.color = color
        self.possible_parents = []
        self.children = {}

    def add_parent(self, color):
        self.possible_parents.append(color)

    def add_child(self, color, num):
        self.children[color] = num

    def __repr__(self):
        return f'<Bag {self.color}: {self.possible_parents}>'


def main():
    lines = read()

    bags = {}

    for line in lines:
        outer_bag, inner_bags = line.strip('.').split(' contain ')
        outer_color = outer_bag.replace(' bags', '')

        if inner_bags == 'no other bags':
            continue

        if outer_color not in bags:
            bags[outer_color] = Bag(outer_color)

        inner_colors = [x.rsplit(' ', 1)[0].split(' ', 1) for x in inner_bags.split(', ')]
        for num_str, inner_c in inner_colors:
            if inner_c not in bags:
                bags[inner_c] = Bag(inner_c)
            bags[inner_c].add_parent(outer_color)
            bags[outer_color].add_child(inner_c, int(num_str))

    processed = set()
    stack = ['shiny gold']
    while stack:
        bag = bags[stack.pop()]
        if bag.color in processed:
            continue
        processed.add(bag.color)
        for parent in bag.possible_parents:
            stack.append(parent)

    p1(len(processed) - 1)

    @lru_cache(maxsize=1000)
    def count_inner_bags(color):
        c = 0
        for inner_color, num in bags[color].children.items():
            c += num + num * count_inner_bags(inner_color)
        return c

    p2(count_inner_bags('shiny gold'))
