from utils import read, p1, p2
from string import ascii_letters


def main():
    lines = read()
    c = 0
    for line in lines:
        m = len(line) // 2
        ch = list(set(line[:m]).intersection(set(line[m:])))[0]
        c += ascii_letters.index(ch) + 1

    p1(c)

    c = 0
    for s1, s2, s3 in zip(lines[::3], lines[1::3], lines[2::3]):
        ch = list(set(s1).intersection(set(s2)).intersection(set(s3)))[0]
        c += ascii_letters.index(ch) + 1

    p2(c)
