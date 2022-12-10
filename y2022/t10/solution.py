from utils import read, p1, p2


def main():
    lines = read()
    c = Computer()
    c.load_code(lines)
    c.run()
    p1(sum(c.strengths))
    c.p()


class Computer:

    def __init__(self):
        self.env = {'x': 1}
        self.code = []
        self.line = 0
        self.cycles = 0
        self.strengths = []
        self.d = [
            ['.' for _ in range(40)]
            for _ in range(6)
        ]

    def reset(self):
        for k in self.env:
            self.env[k] = 0
        self.line = 0

    def load_code(self, lines):
        self.code.extend(lines)

    def cyc(self):
        row, col = divmod(self.cycles, 40)
        if self.env['x'] - 1 <= col <= self.env['x'] + 1:
            self.d[row][col] = '#'
        self.cycles += 1

        if (self.cycles - 20) % 40 == 0:
            self.strengths.append(self.cycles * self.env['x'])

    def noop(self):
        self.cyc()
        self.line += 1

    def addx(self, x):
        for _ in range(2):
            self.cyc()
        self.env['x'] += self.toval(x)

        self.line += 1

    def toval(self, x):
        return int(x) if x.lstrip('-').isdigit() else self.env[x]

    def run(self):
        while self.line < len(self.code):
            self.exec_line()

    def exec_line(self):
        instruction = self.code[self.line]
        cmd, *args = instruction.split()
        getattr(self, cmd)(*args)

    def p(self):
        for line in self.d:
            print(''.join(line))
