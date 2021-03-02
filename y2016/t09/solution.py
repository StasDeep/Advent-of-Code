import re

from utils import read, p1, p2


def main():
    line = ''.join(read())
    p1(len(decompress(line)))
    p2(calc_v2_decompressed_length(line))


def decompress(line):
    pointer = 0

    while pointer < len(line):
        match = re.match(r'\((\d+)x(\d+)\)', line[pointer:])
        if match:
            length, times = map(int, match.groups())
            match_text = match.group(0)
            match_end_idx = pointer + len(match_text)
            text_to_repeat = line[match_end_idx:match_end_idx+length]
            line = line[:pointer] + text_to_repeat * (times - 1) + line[match_end_idx:]
            pointer += len(text_to_repeat) * times
        else:
            pointer += 1

    return line


def calc_v2_decompressed_length(line):
    total_length = 0

    pointer = 0
    while pointer < len(line):
        match = re.match(r'\((\d+)x(\d+)\)', line[pointer:])
        if match:
            length, times = map(int, match.groups())
            match_text = match.group(0)
            match_end_idx = pointer + len(match_text)

            text_to_repeat = line[match_end_idx:match_end_idx + length]
            text_len = calc_v2_decompressed_length(text_to_repeat)

            total_length += text_len * times
            pointer += len(match_text) + length
        else:
            pointer += 1
            total_length += 1

    return total_length


if __name__ == '__main__':
    assert decompress('ADVENT') == 'ADVENT'
    assert decompress('A(1x5)BC') == 'ABBBBBC'
    assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
    assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
    assert decompress('(6x1)(1x3)A') == '(1x3)A'
    assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

    assert calc_v2_decompressed_length('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
    assert calc_v2_decompressed_length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445
