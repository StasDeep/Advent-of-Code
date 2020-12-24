from utils import read, p1, p2


def main(t):
    cups = [int(c) for c in read()[0]]

    # cups_after_100 = run(cups, 100)
    # idx = cups_after_100.index(1)
    # p1("".join(str(x) for x in cups_after_100[idx+1:] + cups_after_100[:idx]))

    # new_cups = cups + list(range(len(cups) + 1, 1000000 + 1))
    new_cups = cups + list(range(len(cups) + 1, 22 + 1))
    cups_after_10m = run(new_cups, 220)
    idx = cups_after_10m.index(1)
    p2(cups_after_10m[(idx + 1) % len(new_cups)] * cups_after_10m[(idx + 2) % len(new_cups)])


def run(cups, num_iterations):
    cups = cups.copy()
    cur_idx = 0
    for move in range(num_iterations):
        # print(move)
        # if move % 100 == 0:
        #     print(move)
        pick_cups = [cups[(cur_idx + i + 1) % len(cups)] for i in range(3)]
        dest = cups[cur_idx]
        while True:
            dest = dest - 1
            if dest < 1:
                dest = len(cups) - dest

            if dest not in pick_cups:
                break

        print(f"-- move {move + 1} --")
        print(f"cups: {' '.join(str(cup) if cup != cups[cur_idx] else f'({cup})' for cup in cups)}")
        # print(f"current: {cups[cur_idx]}")
        print(f"pick up: {', '.join(map(str, pick_cups))}")
        print(f"dest: {dest}")
        print()

        dest_idx = cups.index(dest)
        for i, pickup_cup in enumerate(pick_cups):
            old_idx = (cur_idx + 1) % len(cups)
            del cups[old_idx]
            if old_idx <= dest_idx:
                dest_idx -= 1
            if old_idx <= cur_idx:
                cur_idx -= 1
            new_idx = (dest_idx + i + 1) % len(cups)
            if new_idx <= dest_idx:
                dest_idx += 1
            if new_idx <= cur_idx:
                cur_idx += 1
            cups.insert(new_idx, pickup_cup)

        cur_idx = (cur_idx + 1) % len(cups)

    return cups
