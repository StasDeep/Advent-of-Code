from utils import read, p1, p2
import numpy as np


def main():
    x = read(int)[0]
    spiral = get_spiral(x)

    if spiral == 0:
        p1(0)
    else:
        p1(abs(((spiral * 2 + 1) ** 2 - x) % (spiral * 2) - spiral) + spiral)

    size = 101
    a = np.zeros((size, size)).astype(int)
    center = np.array([size // 2, size // 2])
    a[tuple(center)] = 1

    for i in range(2, (size - 2) ** 2 + 1):
        spiral = get_spiral(i)
        q = (i - (2 * spiral - 1)**2 - 1) // (spiral * 2)  # q is a side of the current spiral layer (0,1,2,3, rtlb)
        offsets = np.array([0, 0])
        offset_angle = ((spiral * 2 + 1) ** 2 - i) % (spiral * 2) - spiral
        #            Y-axis for q1 and q3                 Y-axis for q0 and q2
        offsets[0] = spiral * (q - 2) if q in [1, 3] else offset_angle * (1 - q)
        #            X-axis for q0 and q2                 X-axis for q1 and q3
        offsets[1] = spiral * (1 - q) if q in [0, 2] else offset_angle * (2 - q)
        coords = tuple(center + offsets)
        a[coords] = a[coords[0] - 1:coords[0] + 2, coords[1] - 1:coords[1] + 2].sum()
        if a[coords] > x:
            break

    p2(a[coords])


def get_spiral(x):
    return int(np.ceil((np.ceil(np.sqrt(x)) - 1) / 2))
