import re
from collections import Counter

from utils import read, p1, p2


def main():
    rooms = [Room(line) for line in read()]
    p1(sum(r.sid for r in rooms if r.is_real))
    p2(next(r.sid for r in rooms if r.is_real and "north" in r.dec_name and "pole" in r.dec_name))


class Room:

    def __init__(self, line):
        self.name, self.sid, self.checksum = re.search(r"(.*)-(\d+)\[(.*)]", line).groups()
        self.sid = int(self.sid)

    @property
    def is_real(self):
        c = Counter(self.name.replace("-", ""))
        return "".join(x[0] for x in sorted(c.items(), key=lambda x: (-x[1], x[0]))).startswith(self.checksum)

    @property
    def dec_name(self):
        d = {chr(i + ord("a")): chr((i + self.sid) % 26 + ord("a")) for i in range(26)}
        return "".join(d[c] if c in d else " " for c in self.name)
