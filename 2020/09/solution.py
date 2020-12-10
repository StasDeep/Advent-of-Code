from itertools import combinations

from utils import read


def main():
    lines = read("9_1.txt")

    nums = list(map(int, lines))
    pre = nums[:25]

    for num in nums[25:]:
        s = None
        for a, b in combinations(pre, 2):
            if a + b == num:
                s = num

        if s is None:
            break

        pre = pre[1:] + [num]

    print(num)
    nn = num

    for i in range(len(nums)):
        s = 0
        idx = i
        while s < nn:
            s += nums[idx]
            idx += 1

        if nn == s:
            break


    print(min(nums[i:idx]) + max(nums[i:idx]))


if __name__ == '__main__':
    main()
