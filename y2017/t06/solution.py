from utils import read, p1, p2


def main():
    lines = [int(x) for x in read()[0].split()]

    seen = {}
    while True:
        rep = ' '.join(str(x) for x in lines)
        if rep in seen:
            break
        seen[rep] = len(seen) + 1
        x = max(lines)
        i = lines.index(x)

        a, b = divmod(x, len(lines))
        lines[i] = 0
        for j in range(len(lines)):
            lines[j] += a

        for c in range(b):
            lines[(c + i + 1) % len(lines)] += 1

    p1(len(seen))
    p2(len(seen) - seen[rep] + 1)
