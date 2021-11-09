from utils import read, p1, p2


def main():
    num = int(read()[0])

    nums = list(range(1, num + 1))

    while len(nums) != 1:
        is_odd = len(nums) % 2 != 0

        nums = nums[::2]

        if is_odd:
            nums = nums[1:]

    p1(nums[0])

    nums = list(range(1, num + 1))
    while len(nums) != 1:
        m = len(nums) // 2
        is_odd = len(nums) % 2 != 0
        offset = 1 if is_odd else 2

        updated_half = nums[m + offset::3]
        nums_removed = len(nums) - m - len(updated_half)
        nums = nums[nums_removed:m] + updated_half + nums[:nums_removed]

    p2(nums[0])

