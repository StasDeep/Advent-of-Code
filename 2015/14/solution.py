import re

from utils import read, p1, p2


def main(is_test):
    seconds = 1000 if is_test else 2503
    lines = read()

    m = {}
    for line in lines:
        name, *vals = re.search(r'(.*) can fly (\d+)[^\d]+(\d+)[^\d]+(\d+)', line).groups()
        m[name] = list(map(int, vals))

    p1(max(calc(seconds, *vals) for vals in m.values()))

    all_dists = {name: [calc(sec, *vals) for sec in range(1, seconds + 1)] for name, vals in m.items()}
    best_dists = [max(dists_for_sec) for dists_for_sec in zip(*all_dists.values())]

    p2(max(
        sum(dist == best_dist for dist, best_dist in zip(dists, best_dists))
        for dists in all_dists.values()
    ))


def calc(seconds, speed, time, rest):
    return seconds // (time + rest) * time * speed + min(seconds % (time + rest), time) * speed
