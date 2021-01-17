import itertools
import re

from utils import read, p1, p2


def main():
    lines = read()

    mapping = {}

    for line in lines:
        result = re.search(r'(.*) would (gain|lose) (\d+) .* to (.*)\.', line).groups()
        person1, gain_lose, points, person2 = result
        mapping[(person1, person2)] = (2 * (gain_lose == 'gain') - 1) * int(points)

    p1(calculate_total_happiness(mapping))

    for person in set(itertools.chain.from_iterable(mapping.keys())):
        mapping[(person, 'me')] = mapping[('me', person)] = 0

    p2(calculate_total_happiness(mapping))


def calculate_total_happiness(mapping):
    people = set(itertools.chain.from_iterable(mapping.keys()))
    return max(
        sum(mapping[l, r] + mapping[r, l] for l, r in zip(perm, perm[1:] + tuple([perm[0]])))
        for perm in itertools.permutations(people)
    )
