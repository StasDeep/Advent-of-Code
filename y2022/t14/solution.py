from time import sleep

import numpy
import numpy as np

from utils import read, p1, p2


def main():
    lines = read()

    paths = []
    for l in lines:
        path = []
        coords = l.split(' -> ')
        for c in coords:
            x, y = map(int, c.split(','))
            path.append([y, x])

        paths.append(path)

    max_y = max([coord[0] for path in paths for coord in path]) + 4
    min_x = min([coord[1] for path in paths for coord in path]) - max_y
    s = (0, 500 - min_x)
    for path in paths:
        for i in range(len(path)):
            path[i] = (path[i][0], path[i][1] - min_x)

    max_x = max([coord[1] for path in paths for coord in path])

    a = numpy.array([list('.'*(max_x + max_y*2)) for _ in range(max_y)])
    a[s] = '+'

    for path in paths:
        for c1, c2 in zip(path, path[1:]):
            if c1[0] == c2[0]:
                if c1[1] > c2[1]:
                    c2, c1 = c1, c2
                for i in range(c1[1], c2[1] + 1):
                    a[(c1[0], i)] = '#'
            if c1[1] == c2[1]:
                if c1[0] > c2[0]:
                    c2, c1 = c1, c2
                for i in range(c1[0], c2[0] + 1):
                    a[(i, c1[1])] = '#'



    fell = False
    while not fell:
        curr = s

        # for line in a:
        #     print(''.join(line))
        # print()

        while True:
            next_point = (curr[0] + 1, curr[1])

            if next_point[0] == len(a) - 1:
                fell = True
                break

            if a[next_point] == '.':
                curr = next_point
                continue

            next_point = (next_point[0], next_point[1] - 1)

            if a[next_point] == '.':
                curr = next_point
                continue

            next_point = (next_point[0], next_point[1] + 2)

            if a[next_point] == '.':
                curr = next_point
                continue
            a[curr] = 'o'
            break

    p1(np.count_nonzero(a == 'o'))

    a[max_y - 2] = '#'
    finished = False
    while not finished:
        curr = s

        # for line in a:
        #     print(''.join(line))
        # print()

        while True:
            next_point = (curr[0] + 1, curr[1])

            if a[next_point] == '.':
                curr = next_point
                continue

            next_point = (next_point[0], next_point[1] - 1)

            if a[next_point] == '.':
                curr = next_point
                continue

            next_point = (next_point[0], next_point[1] + 2)

            if a[next_point] == '.':
                curr = next_point
                continue
            a[curr] = 'o'
            if curr == s:
                finished = True
            break

    p2(np.count_nonzero(a == 'o'))
