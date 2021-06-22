from utils import read, p1, p2


def main(is_test, s):
    # 1 for safe, 0 for trap
    first_row = [1 if c == "." else 0 for c in read()[0]]

    rows_target = 10 if is_test else 40
    p1(sum(sum(row) for row in get_full_map(first_row, rows_target)))
    p2(sum(sum(row) for row in get_full_map(first_row, 400_000)))


def get_next_row(row):
    ext_row = [1] + row + [1]

    new_row = []
    for left, center, right in zip(ext_row, ext_row[1:], ext_row[2:]):
        if left ^ right:
            new_row.append(0)
        else:
            new_row.append(1)

    return new_row


def get_full_map(first_row, target: int):
    rows = [first_row]

    while len(rows) < target:
        rows.append(get_next_row(rows[-1]))

    return rows
