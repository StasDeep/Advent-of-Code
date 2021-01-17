import math

from utils import read, p1, p2


def main():
    lines = read()

    s = 0
    for line in lines:
        l, w, h = map(int, line.split('x'))
        s += 2 * l * w + 2 * w * h + 2 * h * l + math.prod(sorted([l, w, h])[:2])

    p1(s)

    s = 0
    for line in lines:
        l, w, h = map(int, line.split('x'))
        s += sum(sorted([l, w, h])[:2]) * 2
        s += l * w * h

    p2(s)
