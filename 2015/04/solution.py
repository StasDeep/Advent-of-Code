from hashlib import md5

from utils import read, p1, p2


def main():
    secret = read()[0]

    p1(find_hash_with_lead_zeroes(secret, 5))
    p2(find_hash_with_lead_zeroes(secret, 6))


def find_hash_with_lead_zeroes(secret, num_zeroes):
    expected = '0' * num_zeroes

    i = 1
    while True:
        h = md5()
        h.update(f'{secret}{i}'.encode('ascii'))
        if h.hexdigest()[:num_zeroes] == expected:
            return i
        i += 1
