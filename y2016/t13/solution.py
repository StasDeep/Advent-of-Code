from utils import read, p1, p2


def main(is_test):
    designer_num = int(read()[0])

    if is_test:
        destination_to_reach = (4, 7)
    else:
        destination_to_reach = (39, 31)

    queue = [(1, 1)]
    distances = {(1, 1): 0}

    while destination_to_reach not in distances:
        pos = queue.pop(0)
        dist = distances[pos]

        for sy, sx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = (pos[0] + sy, pos[1] + sx)

            if next_pos[0] < 0 or next_pos[1] < 0:
                continue

            if next_pos not in distances and not is_wall(next_pos[0], next_pos[1], designer_num):
                distances[next_pos] = dist + 1
                queue.append(next_pos)

    p1(distances[destination_to_reach])
    p2(sum(dist <= 50 for dist in distances.values()))


cache = {}


def is_wall(y, x, designer_num):
    key = (y, x, designer_num)
    if key not in cache:
        n = x * x + 3 * x + 2 * x * y + y + y * y + designer_num
        cache[key] = bin(n).count("1") % 2 == 1
    return cache[key]
