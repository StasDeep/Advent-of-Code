from utils import read, p1, p2


def main():
    lines = read()

    parts = [x.split(" | ") for x in lines]
    parts = [(x.split(), y.split()) for x, y in parts]

    p1(sum(
        sum(len(d) in [2,3,4,7] for d in fourdigits)
        for _, fourdigits in parts
    ))

    p2(sum(get_output(*x) for x in parts))


def get_output(digits, output):
    all_sets = [set(dig) for dig in digits]
    segs = {x: None for x in range(7)}
    digs = {x: None for x in range(10)}
    digs[1] = next(s for s in all_sets if len(s) == 2)
    digs[4] = next(s for s in all_sets if len(s) == 4)
    digs[7] = next(s for s in all_sets if len(s) == 3)
    digs[8] = next(s for s in all_sets if len(s) == 7)
    segs[0] = digs[7].difference(digs[1]).pop()

    segs046 = digs[8].difference(digs[4])
    digs[2] = next(s for s in all_sets if len(s) == 5 and segs046.issubset(s))

    segs15 = digs[8].difference(digs[2])
    segs[5] = next(seg for seg in segs15 if seg in digs[1])
    segs[1] = next(seg for seg in segs15 if seg not in digs[1])
    segs[2] = next(seg for seg in digs[1] if seg != segs[5])
    digs[3] = next(s for s in all_sets if segs[1] not in s and s not in (digs[1], digs[2], digs[7]))
    segs[4] = next(seg for seg in digs[8].difference(digs[3]) if seg != segs[1])

    digs59 = [s for s in all_sets if segs[4] not in s and s not in (digs[1], digs[3], digs[4], digs[7])]
    digs[5], digs[9] = sorted(digs59, key=lambda s: len(s))

    segs[3] = next(seg for seg in digs[4] if seg not in (segs[1], segs[2], segs[5]))
    digs[0] = digs[8].difference({segs[3]})
    digs[6] = next(s for s in all_sets if s not in digs.values())

    segs[6] = next(seg for seg in digs[8] if seg not in segs.values())

    print("\ndigs", {d: "".join(s) for d, s in digs.items()})
    print(digits)
    print(segs)
    print(output)

    for code in output:
        print(code)
        next(str(dig) for dig, segments in digs.items() if set(code) == segments)
    output_digits = [
        next(str(dig) for dig, segments in digs.items() if set(code) == segments) for code in output
    ]

    x = int("".join(output_digits))
    print(x)

    return x

