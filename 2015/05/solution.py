from utils import read, p1, p2


def main():
    lines = read()

    p1(sum(is_nice(line) for line in lines))
    p2(sum(is_really_nice(line) for line in lines))


def is_nice(line):
    vowel_count = sum(line.count(vowel) for vowel in 'aeiou')
    has_doubles = any(x == y for x, y in zip(line, line[1:]))
    has_stop_comb = any(comb in line for comb in ['ab', 'cd', 'pq', 'xy'])
    return vowel_count >= 3 and has_doubles and not has_stop_comb


def is_really_nice(line):
    all_pairs = ["".join([x, y]) for x, y in zip(line, line[1:])]
    has_pair_twice = any(line.count(pair) >= 2 for pair in all_pairs)
    has_triple_borders = any(x == y for x, y in zip(line, line[2:]))
    return has_pair_twice and has_triple_borders
