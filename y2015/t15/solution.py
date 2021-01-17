import re

from utils import read, p1, p2


def main():
    lines = read()

    ings = []
    for line in lines:
        nums = re.search(r".+:.*?([-\d]+).*?([-\d]+).*?([-\d]+).*?([-\d]+).*?([-\d]+)", line).groups()
        ings.append(list(map(int, nums)))

    best_with_500 = None
    best = None
    for amounts in amounts_that_sum_to(100, n=len(ings)):
        score = 1
        for i in range(4):
            score *= max(sum(amounts[j] * ings[j][i] for j in range(len(amounts))), 0)

        if best is None or score > best:
            best = score

        total_cals = sum(amounts[j] * ings[j][-1] for j in range(len(amounts)))
        if total_cals == 500 and (best_with_500 is None or score > best_with_500):
            best_with_500 = score

    p1(best)
    p2(best_with_500)


def amounts_that_sum_to(sum_to: int, n: int):
    if sum_to == 0:
        yield tuple(0 for _ in range(n))
        return

    if n == 0:
        return

    for x in range(0, sum_to + 1):
        for rest in amounts_that_sum_to(sum_to - x, n - 1):
            yield tuple((x,) + rest)
