from utils import read, p1, p2


def main():
    lines = read()

    triangles = [[int(x) for x in line.strip().split()] for line in lines]
    p1(sum(is_possible_triangle(triangle) for triangle in triangles))

    c = 0
    for i in [0, 1, 2]:
        for t1, t2, t3 in zip(triangles[::3], triangles[1::3], triangles[2::3]):
            c += int(is_possible_triangle([t1[i], t2[i], t3[i]]))
    p2(c)


def is_possible_triangle(lengths):
    a, b, c = sorted(lengths)
    return a + b > c
