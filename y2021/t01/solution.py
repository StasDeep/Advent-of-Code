from utils import read, p1, p2


def main():
    nums = read(int)
    p1(sum(y > x for x, y in zip(nums, nums[1:])))
    windows = [sum(x) for x in zip(nums, nums[1:], nums[2:])]
    p2(sum(y > x for x, y in zip(windows, windows[1:])))
