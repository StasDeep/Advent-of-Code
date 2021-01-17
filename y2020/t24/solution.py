import re

import numpy as np

from utils import read, p1, p2

# This is the first way to implement hexagonal grid that came to my mind.
# A pyramid shape of size 3 is represented like this:
# [ ] [x] [ ]
# [x] [x] [ ]
# [x] [x] [x]
# If you shift even rows 0.5 cells to the right (or odd rows 0.5 to the left),
# you'll get a better visualisation of how it works.
# [ ] [x] [ ]
#   [x] [x] [ ]
# [x] [x] [x]
moves = {
    "e": (0, -1),
    "w": (0, 1),
    "se": (1, 0),
    "sw": (1, 1),
    "ne": (-1, -1),
    "nw": (-1, 0),
}


def main():
    lines = read()

    # This size should be enough for the size of task input. This is just faster
    # to implement than trimming/appending rows
    size = 200
    arr = np.zeros((size, size), dtype=bool)
    for line in lines:
        instructions = re.findall("(e|se|sw|ne|nw|w)", line)

        # Reference point is in the middle of the grid
        y, x = size // 2, size // 2
        for i in instructions:
            y += moves[i][0]
            x += moves[i][1]

        arr[y, x] = not arr[y, x]

    p1(np.sum(arr))

    for i in range(100):
        black_neighbors = np.zeros(shape=arr.shape, dtype=int)
        # Using np.argwhere is faster than iterating all cells and checking if each one is True
        for y, x in np.argwhere(arr):
            for y_move, x_move in moves.values():
                black_neighbors[y + y_move, x + x_move] += 1

        # Make cell black if it is:
        # - black and has exactly 1 or 2 black neighbors
        # - white and has exactly 2 black neighbors
        arr = (
            (arr & ((black_neighbors == 1) | (black_neighbors == 2)))
            |
            (~arr & (black_neighbors == 2))
        )

    p2(np.sum(arr))
