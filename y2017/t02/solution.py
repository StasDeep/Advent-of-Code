from utils import read, p1, p2


def main(autosubmit):
    lines = read()

    c = 0
    c2 = 0
    for nums in lines:
        nums = list(map(int, nums.split()))
        c += max(nums) - min(nums)
        from itertools import combinations
        for n1, n2 in combinations(nums, 2):
            n1, n2 = sorted([n1, n2])
            if n2 % n1 == 0:
                c2 += n2 // n1

    p1(c)
    p2(c2)
