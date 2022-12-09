from collections import defaultdict

from utils import read, p1, p2


def main():
    lines = read()
    d = defaultdict(bool)
    hc = [0, 0]
    tc = [0, 0]
    d[tuple(tc)] = True
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

        for i in range(n):
            hc = [hc[0] + di[0], hc[1] + di[1]]

            if hc[0] == tc[0] or hc[1] == tc[1]:
                if abs(hc[0] - tc[0]) == 2 or abs(hc[1] - tc[1]) == 2:
                    tc = [tc[0] + di[0], tc[1] + di[1]]
                    d[tuple(tc)] = True
            elif abs(hc[0] - tc[0]) > 1:
                tc[1] = hc[1]
                tc[0] = hc[0] + 1 * (1 if tc[0] > hc[0] else -1)
                d[tuple(tc)] = True

            elif abs(hc[1] - tc[1]) > 1:
                tc[0] = hc[0]
                tc[1] = hc[1] + 1 * (1 if tc[1] > hc[1] else -1)
                d[tuple(tc)] = True

    p1(len(d))

    d = defaultdict(bool)
    coords = [
        [0, 0]
        for _ in range(10)
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
        orig_di = di
        for j in range(n):
            coords[0] = [coords[0][0] + di[0], coords[0][1] + di[1]]
            for i in range(9):
                # print(i, coords, di)
                hc = coords[i]
                tc = coords[i+1]
                # if i == 8:
                #     print(hc, tc)
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

                # elif abs(hc[1] - tc[1]) > 1:
                #     coords[i+1][0] = tc[0] + 1 * (-1 if tc[0] > hc[0] else 1)
                #     coords[i+1][1] = hc[1] + 1 * (1 if tc[1] > hc[1] else -1)
            d[tuple(coords[-1])] = True
            print(instr, coords)

    p2(len(d))
