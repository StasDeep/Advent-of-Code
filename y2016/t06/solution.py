from collections import Counter

from utils import read, p1, p2


def main():
    lines = read()
    p1(''.join(Counter(chars).most_common()[0][0] for chars in zip(*lines)))
    p2(''.join(Counter(chars).most_common()[-1][0] for chars in zip(*lines)))
