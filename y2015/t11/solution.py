from utils import read, p1, p2
import string


def main():
    line = read()[0]
    idxs = [string.ascii_lowercase.index(ch) for ch in line]

    found_one = False
    while True:
        carry = 1
        for i in reversed(range(0, len(idxs))):
            if not carry:
                break
            carry, idxs[i] = divmod(idxs[i] + carry, len(string.ascii_lowercase))

        for i, idx in enumerate(idxs[:]):
            if string.ascii_lowercase[idx] in "iol":
                for j in range(i + 1, len(idxs)):
                    idxs[j] = len(string.ascii_lowercase) - 1
                break

        if is_seq_valid(idxs):
            if not found_one:
                p1("".join(string.ascii_lowercase[i] for i in idxs))
                found_one = True
            else:
                p2("".join(string.ascii_lowercase[i] for i in idxs))
                break


def is_seq_valid(seq):
    has_triples = False
    for c1, c2, c3 in zip(seq, seq[1:], seq[2:]):
        if c3 - c2 == 1 and c2 - c1 == 1:
            has_triples = True
            break

    has_iol = any(stop in seq for stop in [string.ascii_lowercase.index(ch) for ch in "iol"])

    num_doubles = 0
    s = "".join(string.ascii_lowercase[i] for i in seq)
    skip = False
    for c1, c2 in zip(s, s[1:]):
        if skip:
            skip = False
            continue
        if c1 == c2:
            num_doubles += 1
            skip = True

    return has_triples and not has_iol and num_doubles >= 2
