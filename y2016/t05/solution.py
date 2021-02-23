import hashlib
from itertools import count

from utils import read, p1, p2


def main():
    door_id = read()[0]

    pswd1 = ""
    pswd2 = {}
    for i in count():
        if len(pswd1) == 8 and len(pswd2) == 8:
            break

        h = hashlib.md5(f'{door_id}{i}'.encode('utf-8')).hexdigest()

        if h.startswith('00000'):
            if len(pswd1) < 8:
                pswd1 += h[5]

            if h[5].isdigit() and (idx := int(h[5])) < 8 and idx not in pswd2:
                pswd2[idx] = h[6]

    p1(pswd1)
    p2(''.join(pswd2[i] for i in range(8)))
