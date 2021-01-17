from utils import read, p1, p2


def main():
    line = read()[0]
    p1(line.count('(') - line.count(')'))

    c = 0
    for i, ch in enumerate(line):
        if ch == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            p2(i + 1)
            break
