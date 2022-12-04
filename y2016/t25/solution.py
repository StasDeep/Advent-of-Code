from utils import read, p1, p2


def main():
    line2, line3 = read()[1:3]
    x, y = [int(l.split()[1]) for l in [line2, line3]]
    p = x * y
    c = 0
    while c < p:
        c = c * 2 if c % 2 else c * 2 + 1
    p1(c - p)
