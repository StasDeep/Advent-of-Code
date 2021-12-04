from utils import read, p1, p2


def main():
    lines = read()
    d, h = 0, 0
    for x in lines:
        c, n = x.split()
        n = int(n)
        if c[0] == "u":
            d -= n
        elif c[0] == "d":
            d += n
        else:
            h += n

    p1(d*h)

    d, h, a = 0, 0, 0

    for x in lines:
        c, n = x.split()
        n = int(n)
        if c[0] == "u":
            a -= n
        elif c[0] == "d":
            a += n
        else:
            h += n
            d += n * a

    p2(d * h)
