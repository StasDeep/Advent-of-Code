from itertools import permutations
from queue import Queue

import numpy as np

from utils import read, p1, p2


def main():
    a = np.array([list(x) for x in read()])

    coords = {}
    for i in range(10):
        c = next(zip(*np.where(a == str(i))), None)
        if c:
            coords[str(i)] = c

    distances = {}
    for v1, c1 in coords.items():
        q = Queue()
        visited = np.zeros(a.shape).astype(bool)
        q.put((c1, 0))
        visited[c1] = True
        while not q.empty():
            current_coords, dist = q.get()
            current_value = a[current_coords]
            if current_value not in '.#' and current_value != v1:
                distances[(v1, current_value)] = dist
            for offset_y, offset_x in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                potential_coords = (current_coords[0] + offset_y, current_coords[1] + offset_x)
                if not visited[potential_coords] and a[potential_coords] != '#':
                    q.put((potential_coords, dist + 1))
                    visited[potential_coords] = True

    total_distances = []
    for perm in permutations(list(v for v in coords if v != '0')):
        path = ['0'] + list(perm)
        dist = sum(distances[v1, v2] for v1, v2 in zip(path, path[1:]))
        total_distances.append(dist)

    p1(min(total_distances))

    total_distances = []
    for perm in permutations(list(v for v in coords if v != '0')):
        path = ['0'] + list(perm) + ['0']
        dist = sum(distances[v1, v2] for v1, v2 in zip(path, path[1:]))
        total_distances.append(dist)

    p2(min(total_distances))
