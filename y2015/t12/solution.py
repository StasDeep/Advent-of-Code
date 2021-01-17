import json

from utils import read, p1, p2


def main():
    data = json.loads(read()[0])
    p1(get_sum(data))
    p2(get_sum(data, ignore="red"))


def get_sum(data, ignore=None):
    s = 0
    if isinstance(data, list):
        s += sum(get_sum(x, ignore) for x in data)
    if isinstance(data, dict):
        if not ignore or ignore not in data.values():
            s += sum(get_sum(x, ignore) for x in data.values())
    if isinstance(data, int):
        s += data
    return s

