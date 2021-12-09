from math import prod

from utils import read, p1, p2


def main():
    arr = [
        [int(c) for c in line]
        for line in read()
    ]

    height = len(arr)
    width = len(arr[0])

    low_points = []
    c = 0
    for i in range(height):
        for j in range(width):
            adjacent = []

            if i > 0:
                adjacent.append(arr[i - 1][j])
            if i < height - 1:
                adjacent.append(arr[i + 1][j])
            if j > 0:
                adjacent.append(arr[i][j - 1])
            if j < width - 1:
                adjacent.append(arr[i][j + 1])

            if all(arr[i][j] < adj for adj in adjacent):
                c += arr[i][j] + 1
                low_points.append((i, j))

    p1(c)

    basin_sizes = []
    for i, j in low_points:
        basin_sizes.append(find_basin_size(i, j, arr))

    p2(prod(sorted(basin_sizes)[-3:]))


def find_basin_size(i, j, arr):
    height = len(arr)
    width = len(arr[0])
    visited = [[False for _ in range(len(row))] for row in arr]

    def _inner(p, q):
        visited[p][q] = True
        adjacent = []

        if p > 0:
            adjacent.append((p - 1, q))
        if p < height - 1:
            adjacent.append((p + 1, q))
        if q > 0:
            adjacent.append((p, q - 1))
        if q < width - 1:
            adjacent.append((p, q + 1))

        res = 1
        for adj_i, adj_j in adjacent:
            if not visited[adj_i][adj_j] and arr[p][q] <= arr[adj_i][adj_j] and arr[adj_i][adj_j] != 9:
                res += _inner(adj_i, adj_j)

        return res

    ret_val = _inner(i, j)

    return ret_val
