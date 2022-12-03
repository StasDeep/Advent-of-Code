from utils import read, p1, p2


def main():
    elves = read(int, group=True)
    sums = [sum(x) for x in elves]

    p1(max(sums))
    p2(sum(sorted(sums)[-3:]))
