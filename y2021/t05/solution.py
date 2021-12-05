from utils import read, p1, p2


def main():
    lines = read()

    max_x = 0
    max_y = 0
    points = []
    for line in lines:
        left, right = line.split(' -> ')
        x1, y1 = map(int, left.split(','))
        x2, y2 = map(int, right.split(','))

        if max(x1, x2) > max_x:
            max_x = max(x1, x2)
        if max(y1, y2) > max_y:
            max_y = max(y1, y2)

        points.append((x1, y1, x2, y2))

    board = [[0 for _ in range(max_x + 2)] for _ in range(max_y + 2)]

    for x1, y1, x2, y2 in points:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                board[y][x1] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                board[y1][x] += 1

    p1(sum(x > 1 for row in board for x in row))

    for x1, y1, x2, y2 in points:
        if x1 != x2 and y1 != y2:
            x_range = range(x1, x2 + 1) if x2 > x1 else range(x1, x2 - 1, -1)
            y_range = range(y1, y2 + 1) if y2 > y1 else range(y1, y2 - 1, -1)
            for x, y in zip(x_range, y_range):
                board[y][x] += 1

    p2(sum(x > 1 for row in board for x in row))
