from utils import read, p1, p2


def main():
    nums = [int(x) for x in read()[0].split(',')]

    p1(min(sum(abs(x - n) for n in nums) for x in range(min(nums), max(nums) + 1)))
    p2(min(sum(abs(x - n) * (abs(x-n) + 1) // 2 for n in nums) for x in range(min(nums), max(nums) + 1)))

