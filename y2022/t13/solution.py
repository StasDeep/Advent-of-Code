import functools
import json

from utils import read, p1, p2


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        if a > b:
            return False
        return None
    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            res = compare(x, y)
            if res is not None:
                return res
        return compare(len(a), len(b))
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    if isinstance(b, list) and isinstance(a, int):
        return compare([a], b)


def compare_wrap(a, b):
    return 1 if compare(a, b) else -1


def main():
    groups = read(group=True)

    right_idxs = []
    for i, g in enumerate(groups):
        e1 = eval(g[0])
        e2 = eval(g[1])
        if compare(e1, e2):
            print(i + 1)
            right_idxs.append(i + 1)

    p1(sum(right_idxs))

    packets = []
    for g in groups:
        for line in g:
            packets.append(eval(line))

    packets.append([[2]])
    packets.append([[6]])

    s = sorted(packets, key=functools.cmp_to_key(compare_wrap), reverse=True)

    idxs = []
    for i, y in enumerate(s):
        if json.dumps(y) == '[[2]]' or json.dumps(y) == '[[6]]':
            idxs.append(i + 1)

    p2(idxs[1] * idxs[0])
