from utils import read, p1, p2


def main():
    nums = [int(x) if x else None for x in read()]
    elves = [0]
    for num in nums:
        if num is not None:
            elves[-1] += num
        else:
            elves.append(0)

    p1(max(elves))
    p2(sum(sorted(elves)[-3:]))
