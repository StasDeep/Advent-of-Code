from utils import read, p1, p2


def main():
    line = read()[0]
    instructions = line.split(', ')

    visited_locations = set()
    first_to_visit_twice = None

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    coords = [0, 0]
    for i in instructions:
        direction += 1 if i[0] == 'R' else -1
        num_steps = int(i[1:])
        for _ in range(num_steps):
            coords[0] += directions[direction % 4][0]
            coords[1] += directions[direction % 4][1]

            current_coords = tuple(coords)
            if first_to_visit_twice is None and current_coords in visited_locations:
                first_to_visit_twice = current_coords
            visited_locations.add(current_coords)

    p1(sum(map(abs, coords)))
    p2(sum(map(abs, first_to_visit_twice)))
