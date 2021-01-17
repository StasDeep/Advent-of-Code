from itertools import combinations

from utils import read, p1, p2


def main():
    numbers = read(int)

    a, b = find_pair_summing_to(2020, numbers)
    p1(a * b)

    x, y, z = find_combination_summing_to(2020, 3, numbers)
    p2(x * y * z)


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
