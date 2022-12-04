from utils import read, p1, p2


def main():
    pairs = [x.split(',') for x in read()]
    c = 0
    c2 = 0
    for range1, range2 in pairs:
        l1, r1 = [int(x) for x in range1.split('-')]
        l2, r2 = [int(x) for x in range2.split('-')]
        if r1 >= r2 and l1 <= l2 or r2 >= r1 and l2 <= l1:
            c += 1

        if l1 <= r2 <= r1 or l2 <= r1 <= r2:
            c2 += 1
    p1(c)
    p2(c2)

