from utils import read, p1, p2


def find_nth_number(last_num, start_nums):
    last_positions = {}

    for i, num in enumerate(start_nums[:-1]):
        last_positions[num] = i

    prev_num = start_nums[-1]
    for i in range(len(start_nums), last_num):
        if prev_num not in last_positions:
            num = 0
        else:
            num = i - 1 - last_positions[prev_num]
        last_positions[prev_num] = i - 1
        prev_num = num

    return prev_num


def main():
    nums = list(map(int, read()[0].split(",")))
    p1(find_nth_number(2020, nums))
    p2(find_nth_number(30000000, nums))

