import re

import numpy as np

from utils import read, p1, p2


def main():
    lines = read()
    grid = np.zeros([1000, 1000], dtype=bool)

    for line in lines:
        cmd, *coords = re.search(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line).groups()
        x1, y1, x2, y2 = map(int, coords)
        sl = (slice(y1, y2 + 1), slice(x1, x2 + 1))
        if cmd == 'toggle':
            grid[sl] = np.logical_not(grid[sl])
        elif cmd == 'turn on':
            grid[sl] = True
        elif cmd == 'turn off':
            grid[sl] = False

    p1(np.sum(grid))

    grid = np.zeros([1000, 1000], dtype=int)

    for line in lines:
        cmd, *coords = re.search(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line).groups()
        x1, y1, x2, y2 = map(int, coords)
        sl = (slice(y1, y2 + 1), slice(x1, x2 + 1))
        if cmd == 'toggle':
            grid[sl] += 2
        elif cmd == 'turn on':
            grid[sl] += 1
        elif cmd == 'turn off':
            grid[sl] -= 1

        grid = grid.clip(min=0)

    p2(np.sum(grid))
