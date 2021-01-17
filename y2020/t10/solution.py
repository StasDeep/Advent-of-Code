from utils import read, p1, p2


def main():
    lines = read()

    nums = sorted(map(int, lines))
    nums = [0] + nums + [max(nums) + 3]
    diffs = [0, 0, 0]
    for i, j in zip(nums, nums[1:]):
        diffs[j - i - 1] += 1

    p1(diffs[0] * diffs[2])

    m = [0 for _ in nums]
    m[0] = 1

    for i, num in enumerate(nums):
        for offset in [1, 2, 3]:
            plug_idx = i - offset
            if plug_idx >= 0 and num - nums[plug_idx] <= 3:
                m[i] += m[plug_idx]

    p2(m[-1])
