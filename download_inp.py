from os import makedirs, getenv
from pathlib import Path

import fire
import requests


def download_input(year, task):
    p = Path(str(year)) / str(task) / 'input.txt'

    if not p.parent.exists():
        makedirs(p.parent.as_posix(), exist_ok=True)

    with p.open('w') as fh:
        resp = requests.get(
            f'https://adventofcode.com/{year}/day/{task}/input',
            cookies={'session': getenv('AOC_COOKIE')}
        )
        fh.write(resp.text)


if __name__ == '__main__':
    fire.Fire(download_input)
