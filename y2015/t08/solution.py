import re

from utils import read, p1, p2


def clean_line(line):
    line = re.sub(r'\\x[\da-f]{2}', '1', line[1:-1])
    return re.sub(r'\\(.)', '\1', line)


def escape(line):
    return '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'


def main():
    lines = read()
    p1(sum(len(line) for line in lines) - sum(len(clean_line(line)) for line in lines))
    p2(sum(len(escape(line)) for line in lines) - sum(len(line) for line in lines))
