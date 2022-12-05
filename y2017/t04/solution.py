from utils import read, p1, p2


def main():
    lines = read()
    p1(sum(len(x.split()) == len(set(x.split())) for x in lines))
    p2(sum(len(x.split()) == len(set(tuple(sorted(p)) for p in x.split())) for x in lines))
