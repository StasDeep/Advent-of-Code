import re

from utils import read, p1, p2


class Node:

    def __init__(self, size, used, avail, pct):
        self.size = self.parse_int(size)
        self.used = self.parse_int(used)
        self.avail = self.parse_int(avail)
        self.pct = self.parse_int(pct)

    def parse_int(self, val):
        return int(re.sub(r"\D", "", val))

    def __repr__(self):
        return "<Node: size={size}, used={used}, avail={avail}, pct={pct}>".format(**self.__dict__)


def main(s):
    nodes_raw = read()[2:]

    nodes = {}

    for raw_str in nodes_raw:
        fs, size, used, avail, pct = raw_str.split()
        location = tuple(map(int, re.search(r"x(\d+)-y(\d+)", fs).groups()))
        nodes[location] = Node(size, used, avail, pct)

    nodes_used = sorted(nodes.values(), key=lambda node: node.used)
    nodes_avail = sorted(nodes.values(), key=lambda node: node.avail)

    i = 0
    j = 0
    counter = 0
    while i < len(nodes) and j < len(nodes):
        node_a = nodes_used[i]
        node_b = nodes_avail[j]

        if node_a.used == 0:
            i += 1
            continue

        if node_a.used <= node_b.avail:
            counter += len(nodes) - j
            i += 1
        else:
            j += 1

    p1(counter)

    max_avail = max(node.avail for node in nodes.values())
    avail_loc = next(loc for loc, node in nodes.items() if node.avail == max_avail)
    print(avail_loc)

    max_x = max(loc[0] for loc in nodes.keys())
    max_y = max(loc[1] for loc in nodes.keys())
    for y in range(max_y):
        a = []
        for x in range(max_x):
            if x == 0 and y == 0:
                c = "D"
            elif x == max_x - 1 and y == 0:
                c = "G"
            elif (x, y) == avail_loc:
                c = "0"
            elif nodes[(x, y)].used > max_avail:
                c = "#"
            else:
                c = "."

            a.append(c)

        print(" ".join(a))

    # Finding solution by hand is much easier having the grid printed
    # Correct answer is the sum of:
    # 1. length of a path from empty node (0) to goal data (G)
    # 2. 5 * (width - 2)  # this is how the data is being moved horizontally
    # Since there's a wall of nodes with a gap, path 1 is divided into two easy parts:
    # 1.1. Manhattan distance from empty node (0) to the gap in the wall
    # 1.2. Manhattan distance from the gap to the goal data (G)

    # Calculating:
    # 1.1. 4 (to the left) + 9 (to the top) = 13
    # 1.2. 29 (to the right) + 16 (to the top) = 45
    # 2. 5 * (30 - 2) = 140
    # Answer: 13 + 45 + 140 = 198
