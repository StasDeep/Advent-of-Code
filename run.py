import sys

from utils import SolutionRunner


def main():
    if len(sys.argv) == 3:
        year = sys.argv[1]
        task_num = sys.argv[2]
    else:
        year = '2020'
        task_num = '13'

    SolutionRunner(year, task_num).run(with_test=True)


if __name__ == '__main__':
    main()
