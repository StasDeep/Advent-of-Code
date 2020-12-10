import math

from utils import read, p1, p2


def main():
    lines = read()

    p1(find_trees(lines, 3, 1))

    ways = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    traversal_results = [find_trees(lines, *right_down) for right_down in ways]
    p2(math.prod(traversal_results))


def find_trees(lines, right, down):
    c = 0
    for i, line in enumerate(lines[down::down]):
        offset = ((i + 1) * right) % len(line)
        if line[offset] == "#":
            c += 1
    return c
