import re
from copy import deepcopy

import numpy as np

from utils import read, p1, p2


moves = {
    "e": (0, -1),
    "w": (0, 1),
    "se": (1, 0),
    "sw": (1, 1),
    "ne": (-1, -1),
    "nw": (-1, 0),
}


def main(s):
    lines = read()

    arr = np.zeros((1400, 1400), dtype=bool)
    for line in lines:
        instructions = re.findall("(e|se|sw|ne|nw|w)", line)
        y, x = 700, 700
        for i in instructions:
            y += moves[i][0]
            x += moves[i][1]

        arr[y, x] = not arr[y, x]

    p1(np.sum(arr))

    for i in range(100):
        black_neighbors = np.zeros(shape=arr.shape, dtype=int)
        for (y, x), _ in np.ndenumerate(arr):
            if arr[y, x]:
                for y_move, x_move in moves.values():
                    black_neighbors[y + y_move, x + x_move] += 1

        arr = (
            (arr & ((black_neighbors == 1) | (black_neighbors == 2)))
            |
            (~arr & (black_neighbors == 2))
        )
        print(i, np.sum(arr))

    p2(np.sum(arr))
