from utils import read, p1, p2


def main():
    lines = read()

    seats = []
    for line in lines:
        row_info = line[:-3]
        col_info = line[-3:]
        row_num = int(row_info.replace('F', '0').replace('B', '1'), 2)
        col_num = int(col_info.replace('L', '0').replace('R', '1'), 2)
        seat_id = row_num * 8 + col_num
        seats.append(seat_id)

    p1(max(seats))

    seats = sorted(seats)
    for s1, s2 in zip(seats, seats[1:]):
        if s2 - s1 == 2:
            p2(s2 - 1)
