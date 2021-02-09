from utils import p1


def main():
    row, col = 2978, 3083

    x = 20151125
    for _ in range((row + col - 1) * (row + col - 2) // 2 + col - 1):
        x = (x * 252533) % 33554393

    p1(x)
