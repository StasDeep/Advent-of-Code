from utils import read, p1, p2


def main():
    a = [[int(x) for x in line.strip().split()] for line in read()]
    p1(sum(is_valid(*t) for t in a))
    p2(sum(is_valid(a[i], b[i], c[i]) for a, b, c in zip(a[::3], a[1::3], a[2::3]) for i in range(3)))


def is_valid(*lengths):
    return sum(sorted(lengths)[:2]) > max(lengths)
