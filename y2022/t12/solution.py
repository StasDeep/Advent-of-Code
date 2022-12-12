from queue import Queue
from typing import Callable

from utils import read, p1, p2
import numpy as np


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


class Grid:

    def __init__(self, array):
        self.a = array

    @classmethod
    def from_input(cls, lines):
        return cls(np.array([list(x) for x in lines]))

    def find(self, item, multiple=False):
        res = np.argwhere(self.a == item)
        return tuple(res[0]) if not multiple else [tuple(x) for x in res]

    def find_shortest_path(self, start: tuple, end: tuple, can_go_predicate: Callable):
        q = Queue()
        q.put((start, 0))
        visited = {start: True}

        while not q.empty():
            coords, dist = q.get()
            if coords == end:
                return dist

            for y, x in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_coords = (coords[0] + y, coords[1] + x)
                if not self.is_valid_coords(new_coords):
                    continue
                if visited.get(new_coords):
                    continue
                if can_go_predicate(coords, new_coords):
                    visited[new_coords] = True
                    q.put((new_coords, dist + 1))

    def is_valid_coords(self, coords: tuple):
        return 0 <= coords[0] < self.a.shape[0] and 0 <= coords[1] < self.a.shape[1]

    def iter_coords(self):
        for coords, x in np.ndenumerate(self.a):
            yield tuple(coords)
