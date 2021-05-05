import re
from itertools import count

from utils import read, p1, p2


def main():
    lines = read()
    discs = []
    for line in lines:
        num_positions, position = re.search(r"has (\d+).*;.*position (\d+)\.", line).groups()
        discs.append((int(num_positions), int(position)))

    p1(find_time_to_throw(discs))
    p2(find_time_to_throw(discs + [(11, 0)]))


def find_time_to_throw(discs):
    for t in count():
        for i, (num_positions, position) in enumerate(discs):
            if (t + i + 1 + position) % num_positions != 0:
                break
        else:
            return t
