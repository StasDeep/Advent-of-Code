from utils import read


def calc(lines, right, down):
    c = 0
    for i, line in enumerate(lines[down::down]):
        offset = ((i + 1) * right) % len(line)
        if line[offset] == "#":
            c += 1
    return c


def main():
    lines = read("3_1.txt")
    c1_1 = calc(lines, 1, 1)
    c3_1 = calc(lines, 3, 1)
    c5_1 = calc(lines, 5, 1)
    c7_1 = calc(lines, 7, 1)
    c1_2 = calc(lines, 1, 2)
    print(c1_1)
    print(c3_1)
    print(c5_1)
    print(c7_1)
    print(c1_2)
    print(c1_1 * c3_1 * c5_1 * c7_1 * c1_2)


if __name__ == '__main__':
    main()
