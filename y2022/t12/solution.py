from helpers.grid import Grid
from utils import read, p1, p2


def main():
    lines = read()
    g = Grid.from_input(lines)
    start = tuple(g.find('S'))
    end = tuple(g.find('E'))
    g.a[start] = 'a'
    g.a[end] = 'z'

    def can_go(c, new_c):
        return ord(g.a[c]) + 1 >= ord(g.a[new_c])

    p1(g.find_shortest_path(start, end, can_go))

    distances = []
    for i, j in g.iter_coords():
        if g.a[i][j] != 'a':
            continue
        d = g.find_shortest_path((i, j), end, can_go)
        if d is not None:
            distances.append(d)

    p2(min(distances))
