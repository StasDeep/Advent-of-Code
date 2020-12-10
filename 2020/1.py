from itertools import combinations

from utils import read


def find_pair_summing_to(desired_sum, numbers):
    seen = [False for _ in range(desired_sum + 1)]
    for x in numbers:
        seen[x] = True

        if seen[desired_sum - x]:
            return x, desired_sum - x


def find_combination_summing_to(desired_sum, combination_size, numbers):
    for comb in combinations(numbers, combination_size):
        if sum(comb) == desired_sum:
            return comb


def main():
    numbers = [int(x) for x in read()]

    a, b = find_pair_summing_to(2020, numbers)
    print('Part 1 answer:', a * b)

    x, y, z = find_combination_summing_to(2020, 3, numbers)
    print('Part 2 answer:', x * y * z)
