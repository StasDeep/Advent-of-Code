from utils import read, p1, p2


def main(s):
    line = read()[0]

    p1(get_checksum(line, 272))
    p2(get_checksum(line, 35651584))


def get_checksum(line, desired_len):
    while len(line) < desired_len:
        new_line = line[::-1].replace("1", "2").replace("0", "1").replace("2", "0")
        line = line + "0" + new_line

    checksum = line[:desired_len]

    while len(checksum) % 2 == 0:
        new_checksum = ""
        for a, b in zip(checksum[::2], checksum[1::2]):
            new_checksum += "1" if a == b else "0"

        checksum = new_checksum

    return checksum
