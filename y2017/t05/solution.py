from utils import read, p1, p2


def main():
    a = read(int)

    c = 0
    i = 0
    while 0 <= i < len(a):
        c += 1
        x = a[i]
        if x >= 3:
            a[i] = x - 1
        else:
            a[i] = x + 1
        i += x

    p2(c)
