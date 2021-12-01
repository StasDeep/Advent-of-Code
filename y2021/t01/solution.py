from utils import read, p1, p2


def main():
    ns = read(int)

    p1(sum(y > x for x, y in zip(ns, ns[1:])))

    w = [sum([x,y,z]) for x, y, z in zip(ns, ns[1:], ns[2:])]

    p2(sum(y > x for x, y in zip(w, w[1:])))
