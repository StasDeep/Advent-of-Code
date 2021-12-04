from utils import read, p1, p2


def main():
    lines = read()
    import collections
    xs = list(zip(*lines))
    first = ''
    second = ''
    for x in xs:
        c = collections.Counter(x)
        first += c.most_common(1)[0][0]
        second += c.most_common()[-1][0]

    p1(int(first, 2) * int(second, 2))

    first = None
    first_seqs = lines
    second = None
    second_seqs = lines
    cur = 0
    while True:
        if first is None:
            c = collections.Counter([line[cur] for line in first_seqs])

            res = c.most_common()
            if len(res) > 1:
                (most_c, m), (least_c, n) = res
                if m == n:
                    most_c = '1'
            else:
                most_c = res[0][0]

            first_seqs = [y for y in first_seqs if y[cur] == most_c]
            if len(first_seqs) == 1:
                first = first_seqs[0]

        if second is None:
            c = collections.Counter([line[cur] for line in second_seqs])

            res = c.most_common()
            if len(res) > 1:
                (most_c, m), (least_c, n) = res
                if m == n:
                    least_c = '0'
            else:
                least_c = res[0][0]
            second_seqs = [y for y in second_seqs if y[cur] == least_c]
            if len(second_seqs) == 1:
                second = second_seqs[0]

        if first is not None and second is not None:
            break

        cur += 1

    p2(int(first, 2) * int(second, 2))

