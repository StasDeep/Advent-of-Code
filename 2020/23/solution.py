from itertools import count

from utils import read, p1, p2


def main():
    cups = [int(c) for c in read()[0]]

    after_100 = run(cups, 100)
    p1("".join(map(str, after_100[:-1])))

    # million_cups = cups + list(range(len(cups) + 1, 1000000 + 1))
    # after_10m = run(million_cups, 10000000)
    # p2(after_10m[0] * after_10m[1])


def run(cups, num_iterations):
    d = {c1: c2 for c1, c2 in zip(cups, cups[1:] + [cups[0]])}
    cur = cups[0]
    for x in range(num_iterations):
        c1 = d[cur]
        c2 = d[c1]
        c3 = d[c2]
        pickup = [c1, c2, c3]
        dest = next(
            cup for i in count(1)
            if (cup := cur - i if (cur - i > 0) else len(cups) + (cur - i)) not in pickup
        )

        d[cur], d[c3], d[dest] = d[c3], d[dest], d[cur]

        cur = d[cur]

    result = []
    c = 1
    while True:
        result.append(d[c])
        c = d[c]
        if c == 1:
            break
    return result
