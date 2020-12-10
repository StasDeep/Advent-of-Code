import inspect
import re
from importlib import import_module
from pathlib import Path


def read():
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])

    with (Path(mod.__file__).parent / 'input.txt').open() as fh:
        return [line.strip() for line in fh.readlines() if line]


def p1(*args):
    print('Part 1 answer:', *args)


def p2(*args):
    print('Part 2 answer:', *args)


class SolutionRunner:

    def __init__(self, year, task_num):
        self.year = year
        self.task_num = task_num

        self.solution_module = None
        self.is_test_run = False

        self.expected_answers_for_test = []
        self.actual_answers_for_test = [None, None]

    def run(self, with_test=True):
        print(f'AoC-{self.year}. Task #{self.task_num}')

        self.solution_module = import_module(f'{self.year}.{self.task_num}.solution')

        # Patch common functions used in solution
        self.solution_module.__dict__['read'] = self.read
        self.solution_module.__dict__['p1'] = self.p1
        self.solution_module.__dict__['p2'] = self.p2

        solve_func = vars(self.solution_module)['main']

        # Don't do test run if it is explicitly said so
        # or there is no input file
        if with_test and self.get_input_lines('test') is not None:
            self.is_test_run = True
            solve_func()
            self.is_test_run = False

        solve_func()

    def read(self):
        lines = self.get_input_lines(use_test=self.is_test_run)

        if not self.is_test_run:
            return lines

        # Find expected answers for test
        answers = re.split('\n=+\n', '\n'.join(lines))[-1].strip().split('\n')

        # If there are no expected answers, don't do anything
        if len(answers) == len(lines):
            return lines

        self.expected_answers_for_test = answers

        # Return lines before the answers for test
        return lines[:-len(self.expected_answers_for_test) - 1]

    def p1(self, answer):
        self.check_and_print_answer(answer, 1)

    def p2(self, answer):
        self.check_and_print_answer(answer, 2)

    def check_and_print_answer(self, answer, part_num):
        if self.is_test_run:
            self.actual_answers_for_test[part_num - 1] = answer
        else:
            additional_print = []

            if self.expected_answers_for_test and len(self.expected_answers_for_test) >= part_num:
                actual = str(self.actual_answers_for_test[part_num - 1])
                expected = str(self.expected_answers_for_test[part_num - 1])
                is_test_passing = actual == expected

                if is_test_passing:
                    additional_print.append('(test: OK)')
                else:
                    additional_print.append(
                        f'(expected: {repr(expected)}; actual: {repr(actual)})'
                    )
            elif self.actual_answers_for_test:
                test_answer = self.actual_answers_for_test[part_num - 1]
                additional_print.append(f'(test answer: {test_answer})')

            print(f'Part {part_num} answer:', answer, *additional_print)

    def get_input_lines(self, use_test):
        p = Path(self.solution_module.__file__)

        if use_test:
            input_file = p.parent / 'input_test.txt'
        else:
            input_file = p.parent / 'input.txt'

        if input_file.exists():
            with input_file.open() as fh:
                return [line.rstrip() for line in fh.readlines() if line]

        return None
