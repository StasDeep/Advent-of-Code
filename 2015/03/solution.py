from utils import read, p1, p2


def main():
    line = read()[0]

    p1(len(get_visited(line)))

    santa_visited = get_visited(line[::2])
    robosanta_visited = get_visited(line[1::2])
    p2(len(santa_visited | robosanta_visited))


def get_visited(directions):
    directions_map = {'v': (-1, 0), '^': (1, 0), '>': (0, 1), '<': (0, -1),}
    cur = (0, 0)
    visited = {cur}
    for d in directions:
        y, x = directions_map[d]
        cur = (cur[0] + y, cur[1] + x)
        visited.add(cur)
    return visited
