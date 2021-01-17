import math
from itertools import count

from utils import read, p1, p2


def main():
    lines = read()
    time_start = int(lines[0])
    nums = [int(num) if num != 'x' else None for num in lines[1].split(',')]

    for t in count(time_start):
        bus_id = next((num for num in nums if num is not None and t % num == 0), None)
        if bus_id is not None:
            p1((t - time_start) * bus_id)
            break

    # Adder is the number that fulfills conditions for remainders:
    # 0 for the 1st bus
    # 1 for the 2nd bus etc.
    # Eventually, this number contains the answer
    adder = 0

    # Multiplier contains the product of seen numbers.
    # It allows to quickly jump between numbers that fulfill remainder conditions.
    # I.e. if adder fulfills conditions for the 1st, 2nd and 3rd numbers,
    # multiplier contains the product of these 3 numbers
    multi = nums[0]
    for i, num in enumerate(nums):
        if num is None or num == multi:
            continue

        for x in count(0):
            if (x * multi + adder) % num == (num - i) % num:
                break

        # x contains a number that fulfills remainder condition for the current number `num`.
        # By multiplying it by `multi` (which consists of the product of all previous numbers),
        # the previous remainders will stay unchanged after being added to adder.
        # I.e. `adder` equal to 102 fulfills following remainder conditions:
        #   adder % 17 = 0
        #   adder % 13 = 11
        # In this case, `multi` would be a product `13 * 17`, which means that
        # no matter what the value of `x` is, all conditions will be still fulfilled
        adder += multi * x

        # For the AoC task input which contains only prime numbers in its input,
        # using just `multi * num` is enough. However, in a more general case,
        # least common multiple should be used (test case: `8,x,14,x,10`),
        # otherwise the "jumps" will be too long, skipping possibly correct `x` values
        multi = multi * num // math.gcd(multi, num)

    p2(adder)
