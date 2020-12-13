import sys
from pathlib import Path

from utils import SolutionRunner


def main():
    for year, task_num in get_tasks_from_argv():
        SolutionRunner(year, task_num).run()
        print()


def get_tasks_from_argv():
    if len(sys.argv) == 3:
        tasks = [[sys.argv[1], sys.argv[2]]]
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == 'all':
            p = Path()
        else:
            p = Path(arg)
        tasks = [py_path.as_posix().split('/')[:2] for py_path in p.rglob('solution.py')]
    else:
        all_python_paths = [py_path for py_path in Path().rglob('solution.py')]
        latest_path = sorted(all_python_paths, key=lambda p: p.stat().st_mtime)[-1]
        tasks = [latest_path.as_posix().split('/')[:2]]

    return sorted(tasks)


if __name__ == '__main__':
    main()
