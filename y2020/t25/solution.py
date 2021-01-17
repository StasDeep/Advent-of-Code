from itertools import count

from utils import read, p1


def main():
    cpk, dpk = [int(x) for x in read()]

    subj = 1
    for x in count(1):
        subj = (subj * 7) % 20201227
        if subj == cpk:
            p1(pow(dpk, x, 20201227))
            break
