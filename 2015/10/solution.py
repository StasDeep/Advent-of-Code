from utils import read, p1, p2


def main():
    line = read()[0]

    p1(len(find_nth_elem(40, line)))
    p2(len(find_nth_elem(50, line)))


# TODO: Try to break into "compounds": https://www.youtube.com/watch?v=ea7lJkEhytA
def find_nth_elem(n, zero_elem):
    for i in range(n):
        stats = [[0, zero_elem[0]]]
        for ch in zero_elem:
            if ch == stats[-1][1]:
                stats[-1][0] += 1
            else:
                stats.append([1, ch])

        zero_elem = ''.join(str(x[0]) + str(x[1]) for x in stats)

    return zero_elem
