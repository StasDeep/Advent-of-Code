from collections import Counter, defaultdict

from utils import read, p1, p2


def main():
    nums = [int(x) for x in read()[0].split(',')]

    p1(calc(nums, 80))
    p2(calc(nums, 256))


def calc(nums, steps):
    d = defaultdict(int, Counter(nums).items())

    for _ in range(steps):
        temp = d[0]
        for i in range(8):
            d[i] = d[i + 1]
        d[6] += temp
        d[8] = temp

    return sum(d.values())
