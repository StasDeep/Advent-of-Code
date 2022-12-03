from os import makedirs, getenv
from pathlib import Path

import fire
import requests
from bs4 import BeautifulSoup


def download_input(year, task):
    p = Path(f"y{year}") / f"t{task}" / 'input.txt'

    if not p.parent.exists():
        makedirs(p.parent.as_posix(), exist_ok=True)

    with p.open('w') as fh:
        resp = requests.get(
            f'https://adventofcode.com/{year}/day/{task.lstrip("0")}/input',
            cookies={'session': getenv('AOC_COOKIE')}
        )
        fh.write(resp.text)


def submit_answer(year, task_num, part_num, answer):
    resp = requests.post(
        f"https://adventofcode.com/{year}/day/{task_num.lstrip('0')}/answer",
        data=dict(level=part_num, answer=answer),
        cookies={'session': getenv('AOC_COOKIE')}
    )
    soup = BeautifulSoup(resp.text, features="html.parser")
    text = soup.find('article').text
    return {
        'success': "That's the right answer!" in text,
        'text': text
    }


if __name__ == '__main__':
    fire.Fire(download_input)
