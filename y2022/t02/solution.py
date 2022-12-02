from utils import read, p1, p2

SHAPES = {
    'R': 1,
    'P': 2,
    'S': 3,
}

BEATS = {
    'R': 'S',
    'P': 'R',
    'S': 'P',
}

CODE = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}


def main():
    lineups = [x.split() for x in read()]
    s = 0
    for first, second in lineups:
        s += SHAPES[CODE[second]]
        if CODE[first] == CODE[second]:
            s += 3
        elif BEATS[CODE[second]] == CODE[first]:
            s += 6

    p1(s)
    LOSES = {v: k for k, v in BEATS.items()}
    s = 0
    for first, second in lineups:
        if second == 'X':
            shape = BEATS[CODE[first]]
        elif second == 'Y':
            s += 3
            shape = CODE[first]
        elif second == 'Z':
            s += 6
            shape = LOSES[CODE[first]]
        s += SHAPES[shape]

    p2(s)
