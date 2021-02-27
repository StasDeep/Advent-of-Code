import re

import numpy as np

from utils import read, p1, p2


def main():
    lines = read()

    screen = Screen()
    p1(screen.execute(lines).total_on)
    screen.print()


class Screen:

    def __init__(self):
        self.arr = np.zeros((6, 50), dtype=bool)

    def rect(self, width, height):
        self.arr[0:height, 0:width] = True

    def rotate(self, axis, idx, offset):
        if axis == "x":
            self.arr[:, idx] = np.roll(self.arr[:, idx], offset)
        else:
            self.arr[idx, :] = np.roll(self.arr[idx, :], offset)

    def execute(self, instructions):
        for instruction in instructions:
            if "rect" in instruction:
                w, h = re.search(r"rect (\d+)x(\d+)", instruction).groups()
                self.rect(int(w), int(h))
            else:
                axis, idx, offset = re.search(r"rotate .* (.)=(\d+) by (\d+)", instruction).groups()
                self.rotate(axis, int(idx), int(offset))

        return self

    @property
    def total_on(self):
        return self.arr.sum()

    def print(self):
        for row in self.arr:
            print("".join("#" if x else " " for x in row))
