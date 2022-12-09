from collections import defaultdict

from utils import read, p1, p2


def main():
    lines = read()

    for rope_len, func in [(2, p1), (10, p2)]:
        d = defaultdict(bool)
        coords = [
            [0, 0]
            for _ in range(rope_len)
        ]
        d[tuple(coords[-1])] = True
        for instr in lines:
            c, n = instr.split()
            n = int(n)
            if c == 'R':
                di = [0, 1]
            if c == 'L':
                di = [0, -1]
            if c == 'U':
                di = [-1, 0]
            if c == 'D':
                di = [1, 0]

            for j in range(n):
                coords[0] = [coords[0][0] + di[0], coords[0][1] + di[1]]
                for i in range(rope_len - 1):
                    hc = coords[i]
                    tc = coords[i+1]
                    if hc[0] == tc[0] or hc[1] == tc[1]:
                        if abs(hc[0] - tc[0]) > 1:
                            coords[i+1] = [
                                tc[0] + (-1 if tc[0] > hc[0] else 1),
                                tc[1]
                            ]
                        elif abs(hc[1] - tc[1]) > 1:
                            coords[i+1] = [
                                tc[0],
                                tc[1] + (-1 if tc[1] > hc[1] else 1)
                            ]
                    elif abs(hc[0] - tc[0]) > 1 or abs(hc[1] - tc[1]) > 1:
                        coords[i+1][0] = tc[0] + (-1 if tc[0] > hc[0] else 1)
                        coords[i+1][1] = tc[1] + (-1 if tc[1] > hc[1] else 1)

                d[tuple(coords[-1])] = True

        func(len(d))
