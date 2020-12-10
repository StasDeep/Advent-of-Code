from utils import read


def main():
    lines = read("5_1.txt")

    seats = []
    for line in lines:
        row_info = line[:-3]
        col_info = line[-3:]
        row_num = int(row_info.replace('F', '0').replace('B', '1'), 2)
        col_num = int(col_info.replace('L', '0').replace('R', '1'), 2)
        seat_id = row_num * 8 + col_num
        seats.append(seat_id)

    print(max(seats))

    sset = set(seats)
    for x in range(max(seats) + 1):
        if x not in sset:
            print(x)


if __name__ == '__main__':
    main()
