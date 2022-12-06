from utils import read, p1, p2


def main():
    line = read()[0]

    for n, func in [(4, p1), (14, p2)]:
        # for i, x in enumerate(zip(*[line[j:] for j in range(n)])):
        #     if len(set(x)) == n:
        #         break
        for i in range(len(line)):
            if len(set(line[i:i+n])) == n:
                break
        func(i+n)
