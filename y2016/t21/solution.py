import re

from utils import read, p1, p2


def main(is_test, s):
    instructions = [Instruction.from_string(x) for x in read()]

    s = "abcde" if is_test else "abcdefgh"
    s = list(s)

    for i in instructions:
        s = i.apply(s)

    p1("".join(s))

    s = list("decab") if is_test else list("fbgdceah")
    for i in instructions[::-1]:
        print(i.op)
        print(s)
        new_s = i.unapply(s)
        if "".join(i.apply(new_s)) != "".join(s):
            print(i.op, i.args)
            print(s)
            print(new_s)
            raise ValueError
        s = new_s
        print(s)
        print()

    p2("".join(s))


class Instruction:

    def __init__(self, op, args):
        self.op = op
        self.args = args

    def apply(self, s):
        s = s.copy()
        if self.op == "swap position":
            x = int(self.args[0])
            y = int(self.args[1])
            s[x], s[y] = s[y], s[x]
        elif self.op == "swap letter":
            new_s = []
            x, y = self.args
            for c in s:
                if c == x:
                    c = y
                elif c == y:
                    c = x
                new_s.append(c)
            s = new_s
        elif self.op == "rotate":
            steps = int(self.args[1])
            steps = steps if self.args[0] == "right" else len(s) - steps
            s = self.rotate_right(s, steps)
        elif self.op == "rotate based on position":
            x = self.args[0]
            idx = s.index(x)
            steps = idx + 1 if idx < 4 else idx + 2
            s = self.rotate_right(s, steps)
        elif self.op == "reverse positions":
            x = int(self.args[0])
            y = int(self.args[1])
            s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
        elif self.op == "move position":
            x = int(self.args[0])
            y = int(self.args[1])
            c = s.pop(x)
            s.insert(y, c)

        return s

    def unapply(self, s):
        s = s.copy()

        if self.op == "swap position":
            x = int(self.args[0])
            y = int(self.args[1])
            s[x], s[y] = s[y], s[x]
        elif self.op == "swap letter":
            new_s = []
            x, y = self.args
            for c in s:
                if c == x:
                    c = y
                elif c == y:
                    c = x
                new_s.append(c)
            s = new_s
        elif self.op == "rotate":
            steps = int(self.args[1])
            steps = steps if self.args[0] == "right" else len(s) - steps
            s = self.rotate_right(s, -steps)
        elif self.op == "rotate based on position":
            for offset in range(len(s)):
                candidate = self.rotate_right(s, offset)
                if "".join(self.apply(candidate)) == "".join(s):
                    s = candidate
                    break
        elif self.op == "reverse positions":
            x = int(self.args[0])
            y = int(self.args[1])
            s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
        elif self.op == "move position":
            x = int(self.args[0])
            y = int(self.args[1])
            c = s.pop(y)
            s.insert(x, c)

        return s

    def rotate_right(self, s, steps):
        l = len(s)
        steps = steps % l
        s = s + s
        s = s[l - steps: l*2 - steps]
        return s

    @classmethod
    def from_string(cls, s):
        ops = [
            ("swap position", r"swap position (.*) with position (.*)"),
            ("swap letter", r"swap letter (.*) with letter (.*)"),
            ("rotate based on position", r"rotate based on position of letter (.*)"),
            ("rotate", r"rotate (.*) (.*) step"),
            ("reverse positions", r"reverse positions (.*) through (.*)"),
            ("move position", r"move position (.*) to position (.*)"),
        ]

        for op_name, pattern in ops:
            if s.startswith(op_name):
                return Instruction(op_name, re.findall(pattern, s)[0])
