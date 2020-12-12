import inspect
import re
from importlib import import_module
from pathlib import Path


def read(input_type=str):
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])

    return _read_input(Path(mod.__file__).parent / 'input.txt', input_type)


def _read_input(path: Path, input_type=str):
    with path.open() as fh:
        return [input_type(line.rstrip()) for line in fh.readlines() if line]


def p1(*args):
    print('Part 1 answer:', *args)


def p2(*args):
    print('Part 2 answer:', *args)


class SolutionRunner:

    def __init__(self, year, task_num):
        self.year = year
        self.task_num = task_num

        self.solution_module = None
        self.solve_func = None
        self.is_test_run = False
        self.expected_answers_for_test = []
        self.actual_answers_for_test = [None, None]

    def run(self, with_test=True):
        self.solution_module = import_module(f'{self.year}.{self.task_num}.solution')

        # Patch common functions used in solution
        self.solution_module.__dict__['read'] = self.read
        self.solution_module.__dict__['p1'] = self.p1
        self.solution_module.__dict__['p2'] = self.p2

        self.solve_func = vars(self.solution_module)['main']

        print(f'AoC-{self.year}. Task #{self.task_num}')
        # Don't do test run if it is explicitly said so
        # or there is no input file
        if with_test and self.get_input_lines('test') is not None:
            self.is_test_run = True
            try:
                self.run_solution()
            except Exception:
                print('Test exited with an exception')
            self.is_test_run = False

        self.run_solution()

    def run_solution(self):
        if 'is_test' in inspect.getfullargspec(self.solve_func).args:
            self.solve_func(self.is_test_run)
        else:
            self.solve_func()

    def read(self, input_type=str):
        lines = self.get_input_lines(use_test=self.is_test_run)

        if self.is_test_run:
            # Find expected answers for test
            answers = re.split('\n=+\n', '\n'.join(lines))[-1].strip().split('\n')

            # If there are expected answers, remove them from input
            if len(answers) != len(lines):
                self.expected_answers_for_test = answers

                lines = lines[:-len(self.expected_answers_for_test) - 1]

        return list(map(input_type, lines))

    def p1(self, answer):
        self.check_and_print_answer(answer, 1)

    def p2(self, answer):
        self.check_and_print_answer(answer, 2)

    def check_and_print_answer(self, answer, part_num):
        if self.is_test_run:
            self.actual_answers_for_test[part_num - 1] = answer
        else:
            print(f'Part {part_num} answer:', answer, self.get_extra_info(part_num))

    def get_extra_info(self, part_num):
        if self.expected_answers_for_test and len(self.expected_answers_for_test) >= part_num:
            actual = str(self.actual_answers_for_test[part_num - 1])
            expected = str(self.expected_answers_for_test[part_num - 1])
            is_test_passing = actual == expected

            if is_test_passing:
                return '(test: OK)'
            else:
                return f'(test results; expected: {repr(expected)}; actual: {repr(actual)})'

        test_answer = self.actual_answers_for_test[part_num - 1]
        if test_answer is not None:
            return f'(test answer: {test_answer})'

        return ''

    def get_input_lines(self, use_test):
        p = Path(self.solution_module.__file__)

        if use_test:
            input_file = p.parent / 'input_test.txt'
        else:
            input_file = p.parent / 'input.txt'

        if input_file.exists():
            return _read_input(input_file)

        return None
