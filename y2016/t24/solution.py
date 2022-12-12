from itertools import permutations

from utils import read, p1, p2
from y2022.t12.solution import Grid


def main():
    g = Grid.from_input(read())

    coords = {}
    for i in range(10):
        c = g.find(str(i))
        if c:
            coords[str(i)] = c

    distances = {}
    for v1, c1 in coords.items():
        v1_distances = g.find_shortest_path(c1, None, lambda _, new_c: g.a[new_c] != '#')
        for v2, c2 in coords.items():
            if v1 == v2:
                continue
            distances[(v1, v2)] = v1_distances[c2]

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
