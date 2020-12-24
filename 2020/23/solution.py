from itertools import count

from utils import read, p1, p2


def main():
    cups = [int(c) for c in read()[0]]

    after_100 = run(cups, 100)
    p1("".join(str(x) for x in after_100[:-1]))

    million_cups = cups + list(range(len(cups) + 1, 1000000 + 1))
    after_10m = run(million_cups, 10000000)
    p2(after_10m[0] * after_10m[1])


def run(cups, num_iterations):
    d = {c1: c2 for c1, c2 in zip(cups, cups[1:] + [cups[0]])}
    cur = cups[0]
    for x in range(num_iterations):
        x = cur
        pickup = [x := d[x] for _ in range(3)]
        dest = next(
            cup for i in count(1)
            if (cup if (cup := cur - i) > 0 else (cup := len(cups) + cup)) not in pickup
        )

        d[cur], d[pickup[-1]], d[dest] = d[pickup[-1]], d[dest], d[cur]

        cur = d[cur]

    x = 1
    return [x := d[x] for _ in cups]
