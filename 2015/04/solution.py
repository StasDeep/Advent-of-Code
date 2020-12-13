from hashlib import md5
from itertools import count

from utils import read, p1, p2


def main(is_test):
    secret = read()[0]

    p1(find_hash_with_lead_zeroes(secret, 5))

    if not is_test:
        p2(find_hash_with_lead_zeroes(secret, 6))


def find_hash_with_lead_zeroes(secret, num_zeroes):
    expected = '0' * num_zeroes

    for i in count(1):
        h = md5()
        h.update(f'{secret}{i}'.encode('ascii'))
        if h.hexdigest()[:num_zeroes] == expected:
            return i
