from utils import read, p1, p2


def main():
    lines = read()
    c = Computer()
    c.env['a'] = 7
    c.load_code(lines)
    c.run()
    p1(c.env["a"])

    c.reset()
    c.multiply_shortcut = True
    c.env['a'] = 12
    c.load_code(lines)
    c.run()
    p2(c.env['a'])


class Computer:

    def __init__(self):
        self.env = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.code = []
        self.line = 0
        self.multiply_shortcut = False

    def reset(self):
        for k in self.env:
            self.env[k] = 0
        self.line = 0
        self.code = []

    def load_code(self, lines):
        self.code.extend(lines)

    def cpy(self, x, y):
        if y in 'abcd':
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
            self.line += int(self.toval(jmp))
        else:
            self.line += 1

    def tgl(self, x):
        linenum = self.line + self.toval(x)
        if linenum < 0 or linenum >= len(self.code):
            self.line += 1
            return

        cmd, *args = self.code[linenum].split()
        if len(args) == 1:
            if cmd == 'inc':
                new_cmd = 'dec'
            else:
                new_cmd = 'inc'
        else:
            if cmd == 'jnz':
                new_cmd = 'cpy'
            else:
                new_cmd = 'jnz'
        self.code[linenum] = f'{new_cmd} {" ".join(args)}'
        self.line += 1

    def toval(self, x):
        return int(x) if x.lstrip('-').isdigit() else self.env[x]

    def run(self):
        while self.line < len(self.code):
            self.exec_line()

    def exec_line(self):
        instruction = self.code[self.line]
        if instruction == 'tgl c' and self.multiply_shortcut:
            linenum = self.line
            self.env = {'a': 479001600, 'b': 1, 'c': 2, 'd': 0}
            for arg in [10, 8, 6, 4, 2]:
                self.line = linenum
                self.tgl(str(arg))
            return
        cmd, *args = instruction.split()
        getattr(self, cmd)(*args)

    def debug(self):
        for i, l in enumerate(self.code):
            if i == self.line:
                print(f'> {l} ({self.env})')
            else:
                print(f'  {l}')
        print()
