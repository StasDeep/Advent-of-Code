from math import prod

from utils import read, p1, p2


def main():
    groups = read(group=True)
    monkeys = []
    for g in groups:
        monkeys.append(Monkey(g))

    cd = prod([m.divisible_by for m in monkeys])

    c = [0 for m in monkeys]
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                c[i] += 1
                level = monkey.op(item)
                level = level // 3
                level %= cd
                monkeys[monkey.next(level)].items.append(level)
            monkey.items = []
    p1(prod(sorted(c)[-2:]))

    monkeys = []
    for g in groups:
        monkeys.append(Monkey(g))
    c = [0 for m in monkeys]
    for _ in range(10_000):
        for i, monkey in enumerate(monkeys):
            for item in monkey.items:
                c[i] += 1
                level = monkey.op(item)
                level %= cd
                monkeys[monkey.next(level)].items.append(level)
            monkey.items = []
    p2(prod(sorted(c)[-2:]))


class Monkey:

    def __init__(self, lines):
        self.lines = lines
        self.items = [int(x) for x in lines[1].split(': ')[1].split(', ')]
        operation = lines[2].split(': ')[1].split('= ')[1]
        self.op = lambda old: eval(operation)
        self.divisible_by = int(lines[3].split('by ')[1])
        self.if_true = int(lines[4].split('monkey ')[1])
        self.if_false = int(lines[5].split('monkey ')[1])

    def next(self, level):
        return self.if_true if level % self.divisible_by == 0 else self.if_false

    def __repr__(self):
        return str(self.lines[0]) + str(self.items)
