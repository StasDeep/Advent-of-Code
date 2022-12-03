from utils import read, p1, p2


def main():
    sorig = read()[0]
    s = sorig + sorig[0]
    c = 0
    for x, y in zip(s, s[1:]):
        if x == y:
            c += int(x)
    p1(c)

    s = sorig * 2
    c = 0
    for x, y in zip(s[:len(sorig)], s[len(sorig)//2:]):
        if x == y:
            c += int(x)
    p2(c)
