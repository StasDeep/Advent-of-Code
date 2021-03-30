import hashlib
import re
from functools import lru_cache
from itertools import count

from utils import read, p1, p2


@lru_cache(maxsize=1010)
def get_hash_simple(salt, idx):
    return hashlib.md5(f'{salt}{idx}'.encode('utf-8')).hexdigest()


@lru_cache(maxsize=1010)
def get_hash_2016(salt, idx):
    h = hashlib.md5(f'{salt}{idx}'.encode('utf-8')).hexdigest()
    for _ in range(2016):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()
    return h


@lru_cache(maxsize=1010)
def get_triplet_char(h):
    match = re.search(r"(.)\1{2}", h)
    if match:
        return match.group(1)
    return None


@lru_cache(maxsize=16000)
def has_five_in_a_row(h, ch):
    return ch * 5 in h


def main():
    salt = read()[0]
    p1(get_64_index(salt, hash_method=get_hash_simple))
    p2(get_64_index(salt, hash_method=get_hash_2016))


def get_64_index(salt, hash_method):
    keys_found = []

    for i in count():
        h = hash_method(salt, i)
        ch = get_triplet_char(h)

        if ch is not None:
            for j in range(i + 1, i + 1 + 1000):
                next_hash = hash_method(salt, j)
                if get_triplet_char(next_hash) and has_five_in_a_row(next_hash, ch):
                    keys_found.append(h)
                    break

        if len(keys_found) == 64:
            return i
