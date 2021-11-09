from utils import read, p1, p2


def main():
    ranges = read()

    ranges = [
        tuple(map(int, x.split("-"))) for x in ranges
    ]

    ranges.sort()

    num = 0
    i = 0
    while True:
        x, y = ranges[i]
        if num < x:
            break

        if num < y:
            num = y + 1

        i += 1

    p1(num)

    num = 0
    i = 0
    c = 0
    while i < len(ranges):
        x, y = ranges[i]
        if num < x:
            c += 1
            num += 1
            continue
        elif num < y:
            num = y + 1

        i += 1

    if num < 2**32 - 1:
        c += 2**32 - 1 - num

    p2(c)
