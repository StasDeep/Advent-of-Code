from abc import ABC

from utils import read, p1, p2


def main():
    lines = read()

    p1(LeftToRightEvaluator.sum(lines))
    p2(AddBeforeMultEvaluator.sum(lines))


class Evaluator(ABC):

    def evaluate(self, line):
        line_wo_brackets = self.remove_brackets(line)
        return self.evaluate_without_brackets(line_wo_brackets)

    def remove_brackets(self, line):
        top_level_brackets = []
        stack = []
        for i, c in enumerate(line):
            if c == "(":
                stack.append(i)
            elif c == ")":
                start_i = stack.pop()
                if not stack:
                    top_level_brackets.append((start_i, i))

        new_line = line
        for i, j in top_level_brackets:
            new_line = new_line.replace(line[i:j + 1], str(self.evaluate(line[i + 1:j + 1 - 1])), 1)
        return new_line

    def evaluate_without_brackets(self, line):
        raise NotImplemented

    @classmethod
    def sum(cls, lines):
        obj = cls()
        return sum(obj.evaluate(line) for line in lines)


class LeftToRightEvaluator(Evaluator):

    def evaluate_without_brackets(self, line):
        x = line.split()
        res = int(x[0])
        for op, oper in zip(x[1::2], x[2::2]):
            if op == "+":
                res += int(oper)
            elif op == "*":
                res *= int(oper)
        return res


class AddBeforeMultEvaluator(Evaluator):

    def evaluate_without_brackets(self, line):
        while "+" in line:
            x = line.split()
            for oper1, op, oper2 in zip(x[::2], x[1::2], x[2::2]):
                if op == "+":
                    line = line.replace(" ".join([oper1, op, oper2]), str(int(oper1) + int(oper2)), 1)
                    break

        # Only multiplications left
        return eval(line)
