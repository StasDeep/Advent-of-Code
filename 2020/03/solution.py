import math

from utils import read


def find_trees(lines, right, down):
    c = 0
    for i, line in enumerate(lines[down::down]):
        offset = ((i + 1) * right) % len(line)
        if line[offset] == "#":
            c += 1
    return c


def main():
    lines = read()

    print('Part 1 answer', find_trees(lines, 3, 1))

    ways = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    traversal_results = [find_trees(lines, *right_down) for right_down in ways]
    print('Part 2 answer', math.prod(traversal_results))


if __name__ == '__main__':
    main()
