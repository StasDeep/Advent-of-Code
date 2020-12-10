import sys
from importlib import import_module


def main():
    if len(sys.argv) == 3:
        year = sys.argv[1]
        task = sys.argv[2]
    else:
        year = '2020'
        task = '2'

    mod = import_module(f'{year}.{task}')
    solve_func = vars(mod)['main']

    solve_func()


if __name__ == '__main__':
    main()
