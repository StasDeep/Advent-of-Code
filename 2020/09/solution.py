from itertools import combinations

from utils import read, p2, p1


def main(is_test: bool = False):
    pre_size = 5 if is_test else 25
    nums = read(int)
    pre = nums[:pre_size]

    for num in nums[pre_size:]:
        s = None
        for a, b in combinations(pre, 2):
            if a + b == num:
                s = num

        if s is None:
            p1(num)
            break

        pre = pre[1:] + [num]

    nn = num

    for i in range(len(nums)):
        s = 0
        idx = i
        while s < nn:
            s += nums[idx]
            idx += 1

        if nn == s:
            p2(min(nums[i:idx]) + max(nums[i:idx]))
            break
