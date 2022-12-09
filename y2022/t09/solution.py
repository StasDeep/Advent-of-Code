from utils import read, p1, p2

# Use complex numbers as 2d coordinates
DIRS = {"U": +1j, "D": -1j, "L": -1, "R": +1}


def main():
    lines = read()

    for rope_len, func in [(2, p1), (10, p2)]:
        d = {}
        coords = [0 for _ in range(rope_len)]
        for instr in lines:
            c, n = instr.split()
            for j in range(int(n)):
                coords[0] += DIRS[c]
                for i in range(rope_len - 1):
                    head = coords[i]
                    tail = coords[i+1]
                    diff = head - tail
                    # Check if head and tail are in the same column/row
                    if 0 in [diff.real, diff.imag]:
                        if abs(diff.real) > 1:
                            coords[i+1] += (-1 if tail.real > head.real else 1)
                        elif abs(diff.imag) > 1:
                            coords[i+1] += (-1j if tail.imag > head.imag else 1j)
                    elif abs(diff.real) > 1 or abs(diff.imag) > 1:
                        coords[i+1] += (-1 if tail.real > head.real else 1)
                        coords[i+1] += (-1j if tail.imag > head.imag else 1j)

                d[coords[-1]] = True

        func(len(d))
