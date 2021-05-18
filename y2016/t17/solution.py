import hashlib

from utils import read, p1, p2


def main():
    inp = read()[0]

    q = [((0, 0), inp)]

    solutions = []

    while q:
        coords, line = q.pop(0)

        if coords[0] == 3 and coords[1] == 3:
            solutions.append(line)
            continue

        u, d, l, r = [x in "bcdef" for x in hashlib.md5(line.encode('utf-8')).hexdigest()[:4]]

        if u and coords[0] > 0:
            q.append(((coords[0] - 1, coords[1]), line + "U"))

        if d and coords[0] < 3:
            q.append(((coords[0] + 1, coords[1]), line + "D"))

        if l and coords[1] > 0:
            q.append(((coords[0], coords[1] - 1), line + "L"))

        if r and coords[1] < 3:
            q.append(((coords[0], coords[1] + 1), line + "R"))

    p1(solutions[0][len(inp):])
    p2(len(solutions[-1]) - len(inp))
