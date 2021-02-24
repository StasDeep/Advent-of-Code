import re

from utils import read, p1, p2


def main():
    lines = read()
    p1(sum(supports_tls(line) for line in lines))
    p2(sum(supports_ssl(line) for line in lines))


def supports_tls(line):
    supernet, hypernet = (s := re.split(r'(?:\[|\])', line))[::2], s[1::2]
    return any(has_abba(x) for x in supernet) and not any(has_abba(x) for x in hypernet)


def supports_ssl(line):
    supernet, hypernet = (s := re.split(r'(?:\[|\])', line))[::2], s[1::2]
    babs = sum((list(get_babs(x)) for x in supernet), [])
    return any(any(bab in x for bab in babs) for x in hypernet)


def get_babs(x):
    for a, b, c in zip(x, x[1:], x[2:]):
        if a == c and a != b:
            yield b + a + b


def has_abba(x):
    for a, b, c, d in zip(x, x[1:], x[2:], x[3:]):
        if a == d and b == c and a != b:
            return True
    return False
