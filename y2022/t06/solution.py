from utils import read, p1, p2


def main():
    lines = read()[0]

    for n, func in [(4, p1), (14, p2)]:
        for i, x in enumerate(zip(*[lines[j:] for j in range(n)])):
            if len(set(x)) == n:
                break
        func(i+n)
