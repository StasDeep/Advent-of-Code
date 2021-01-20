from itertools import count, combinations
from math import sqrt, prod

from utils import read, p1, p2


def get_prime_factors(number):
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i

    if number > 2:
        prime_factors.append(int(number))

    return prime_factors


def main():
    num = int(read()[0])

    got_p1 = False
    got_p2 = False
    for x in count(1):
        factors = get_prime_factors(x)
        multiples = set(prod(comb) for i in range(len(factors)) for comb in combinations(factors, i + 1)) | {1}
        if not got_p1 and sum(multiples) * 10 >= num:
            p1(x)
            got_p1 = True

        if not got_p2 and sum(y for y in multiples if x / y <= 50) * 11 >= num:
            p2(x)
            got_p2 = True

        if got_p1 and got_p2:
            break
