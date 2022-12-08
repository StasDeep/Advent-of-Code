import numpy as np
from math import prod

from utils import read, p1, p2


def main():
    lines = read()

    a = np.array([list(map(int, x)) for x in lines])
    c = 0
    for i, line in enumerate(a):
        for j, x in enumerate(line):
            if (
                # Check if the item is on edge
                i in [0, len(a) - 1] or j in [0, len(line) - 1]
                # or any of 4 directions are unobstructed
                or np.all(a[i, :j] < x) or np.all(a[i, j+1:] < x) or np.all(a[:i, j] < x) or np.all(a[i+1:, j] < x)
            ):
                c += 1

    p1(c)

    s = 0
    for i, line in enumerate(a):
        for j, x in enumerate(line):
            scores = [0, 0, 0, 0]
            for k, offset in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
                coords = [i + offset[0], j + offset[1]]

                while 0 <= coords[0] < len(a) and 0 <= coords[1] < len(line):
                    scores[k] += 1
                    if not a[tuple(coords)] < x:
                        break
                    coords[0] += offset[0]
                    coords[1] += offset[1]

            n = prod(scores)
            if n > s:
                s = n

    p2(s)
