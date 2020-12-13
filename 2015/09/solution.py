from collections import defaultdict
from itertools import permutations

from utils import read, p1, p2


def main():
    lines = read()

    d = defaultdict(dict)
    for line in lines:
        cities, s = line.split(' = ')
        s = int(s)
        city1, city2 = cities.split(' to ')
        d[city1][city2] = s
        d[city2][city1] = s

    cities = list(d)

    best = None
    worst = None
    for city_order in permutations(cities):
        su = 0
        for city1, city2 in zip(city_order, city_order[1:]):
            su += d[city1][city2]

        if best is None or su < best:
            best = su
        if worst is None or su > worst:
            worst = su

    p1(best)
    p2(worst)
