import math
from itertools import combinations

from utils import p1, p2, read


def main():
    ws = list(map(int, read()))
    # ws = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

    p1(find_best_qe(ws, 3))
    p2(find_best_qe(ws, 4))


def find_best_qe(ws, num_groups):
    best_len = None
    best_qe = None

    expected_sum = sum(ws) // num_groups

    # We care about actual values of only the first group.
    for first_group in get_all_valid_groups(ws, expected_sum):
        # If there's one valid solution found,
        # stop checking as soon as we start getting longer first groups,
        # since longer groups are apriori worse.
        if best_len is not None and len(first_group) > best_len:
            break

        # We don't care about actual values of next groups. Only checking if they exist.
        if exists_full_comb(list(set(ws) - set(first_group)), expected_sum):
            qe = math.prod(first_group)
            if best_qe is None or qe < best_qe:
                best_qe = qe
                best_len = len(first_group)

    return best_qe


def get_all_valid_groups(ws, valid_sum):
    """Generator of all possible groups that sum to the passed number."""
    for length in range(1, len(ws) + 1):
        for comb in combinations(ws, r=length):
            if sum(comb) == valid_sum:
                yield comb


def exists_full_comb(ws, expected_sum):
    """
    Check recursively if it is possible to get a combination of groups
    each having the same passed sum.
    """
    if sum(ws) == expected_sum:
        return True

    for _group in get_all_valid_groups(ws, expected_sum):
        if exists_full_comb([w for w in ws if w not in _group], expected_sum):
            return True

    return False
