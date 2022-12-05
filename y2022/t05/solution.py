import re
import string
from collections import defaultdict

from utils import read, p1, p2


def main():
    lines = read()

    containers = defaultdict(list)
    moves = []
    for line in lines:
        if not line:
            continue
        if line.startswith('move'):
            moves.append(re.findall(r'move (\d+) from (\d+) to (\d+)', line)[0])
        else:
            for i, c in enumerate(line):
                if c in string.ascii_uppercase:
                    containers[str(i//4 + 1)].append(c)

    containers2 = containers.copy()
    for count, fr, to in moves:
        count = int(count)

        for _ in range(count):
            containers[to] = [containers[fr][0]] + containers[to]
            containers[fr] = containers[fr][1:]

        containers2[to] = containers2[fr][:count] + containers2[to]
        containers2[fr] = containers2[fr][count:]

    p1(''.join(containers[i][0] for i in sorted(containers)))
    p2(''.join(containers2[i][0] for i in sorted(containers)))
