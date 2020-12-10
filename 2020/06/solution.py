from utils import read, p1, p2


def main():
    groups = '\n'.join(read()).split('\n\n')

    p1(sum(len(set(group.replace('\n', ''))) for group in groups))

    c = 0
    for group in groups:
        s = None
        for p in group.split('\n'):
            if s is None:
                s = set(p)
            else:
                s = s.intersection(set(p))

        c += len(s)

    p2(c)
