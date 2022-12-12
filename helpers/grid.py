from queue import Queue
from typing import Callable

import numpy as np


class Grid:

    def __init__(self, array):
        self.a = array

    @classmethod
    def from_input(cls, lines):
        return cls(np.array([list(x) for x in lines]))

    def find(self, item, multiple=False):
        res = np.argwhere(self.a == item)
        if len(res):
            return tuple(res[0]) if not multiple else [tuple(x) for x in res]
        return None

    def find_shortest_path(self, start: tuple, end: tuple, can_go_predicate: Callable):
        q = Queue()
        q.put((start, 0))
        visited = {start: True}
        distances = {}
        while not q.empty():
            coords, dist = q.get()
            distances[coords] = dist
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

        if end is None:
            return distances

    def is_valid_coords(self, coords: tuple):
        return 0 <= coords[0] < self.a.shape[0] and 0 <= coords[1] < self.a.shape[1]

    def iter_coords(self):
        for coords, x in np.ndenumerate(self.a):
            yield tuple(coords)
