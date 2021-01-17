from utils import read, p1, p2


def toint(x):
    return int(x.split("_")[0])


def main():
    containers = read()  # input is a little different from the original
    total = 150
    # containers = ["5_1", "5_2", "10", "15", "20"]
    # total = 25

    dp = [[] for _ in range(total + 1)]
    dp[0] = [[]]  # 1 way to get to 0: with no containers used

    for i in range(1, total + 1):
        solutions = set()
        for c in containers:
            if i < toint(c):
                continue

            solutions.update([tuple(sorted(prev + [c])) for prev in dp[i - toint(c)] if c not in prev])

        dp[i] = [list(s) for s in solutions]

    for i, x in enumerate(dp[:50]):
        print(i, ":", x)

    p1(len(dp[total]))

    min_solution_len = min(len(solution) for solution in dp[total])
    p2(sum(len(solution) == min_solution_len for solution in dp[total]))
