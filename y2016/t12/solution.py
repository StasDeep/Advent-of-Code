from utils import read, p1, p2


def main():
    lines = read()
    c = Computer()
    c.load_code(lines)
    c.run()
    p1(c.env["a"])

    c.reset()
    c.env["c"] = 1
    c.run()
    p2(c.env["a"])


class Computer:

    def __init__(self):
        self.env = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.code = []
        self.line = 0

    def reset(self):
        for k in self.env:
            self.env[k] = 0
        self.line = 0

    def load_code(self, lines):
        self.code.extend(lines)

    def cpy(self, x, y):
        self.env[y] = self.toval(x)
        self.line += 1

    def inc(self, x):
        self.env[x] += 1
        self.line += 1

    def dec(self, x):
        self.env[x] -= 1
        self.line += 1

    def jnz(self, x, jmp):
        if self.toval(x):
            self.line += int(jmp)
        else:
            self.line += 1

    def toval(self, x):
        return int(x) if x.isdigit() else self.env[x]

    def run(self):
        while self.line < len(self.code):
            self.exec_line()

    def exec_line(self):
        instruction = self.code[self.line]
        cmd, *args = instruction.split()
        getattr(self, cmd)(*args)
