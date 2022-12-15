import re

from utils import read, p1, p2


def main(is_test, t):
    lines = read()

    t = 10 if is_test else 2000000
    bound = 20 if is_test else 4_000_000

    sensors = []
    beacons = []
    distances = []
    for line in lines:
        res = re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        sx, sy, bx, by = map(int, res[0])
        sensors.append(sx + sy * 1j)
        beacons.append(bx + by * 1j)
        distances.append(abs(sx - bx) + abs(sy - by))

    x_coords = set()
    for s, b in zip(sensors, beacons):
        dist = abs(s.real - b.real) + abs(s.imag - b.imag)
        max_range_at_t = dist - abs(s.imag - t)
        for x in range(int(s.real - max_range_at_t), int(s.real + 1+ max_range_at_t)):
            x_coords.add(x)
    p1(sum(x + t * 1j not in beacons for x in x_coords))

    for s, b, dist in zip(sensors, beacons, distances):
        dist += 1
        for offset in range(int(dist)):
            points = [
                s - dist + offset + offset * 1j,
                s + dist - offset + offset * 1j,
                s - dist + offset - offset * 1j,
                s + dist - offset - offset * 1j,
            ]
            for p in points:
                if not (0 <= p.imag <= bound and 0 <= p.real <= bound):
                    continue
                if any(abs(s2.real - p.real) + abs(s2.imag - p.imag) <= dist2 for s2, b2, dist2 in zip(sensors, beacons, distances)):
                    continue

                p2(int(p.real * 4000000 + p.imag))
                return
