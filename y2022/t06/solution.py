from utils import read, p1, p2
import re


def main():
    lines = read()[0]

    for i, x in enumerate(zip(lines, lines[1:], lines[2:], lines[3:])):
        if len(set(x)) == 4:
            break
    p1(i+4)

    for i, x in enumerate(zip(*[lines[j:] for j in range(14)])):
        if len(set(x)) == 14:
            break
    p2(i+14)
