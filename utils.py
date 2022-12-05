import inspect
import re
import webbrowser
from datetime import datetime
from enum import Enum
from importlib import import_module
from pathlib import Path

import pyperclip

from aoc_api import download_input, submit_answer


def read(input_type=str, group=False):
    if group:
        print('WARNING: `group` is only implemented for run using `run.py`')

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

    class RunModes(Enum):
        SOLUTION_ONLY = 'solution_only'
        TEST_ONLY = 'test_only'
        SOLUTION_TEST = 'solution_and_test'

    def __init__(self, year, task_num):
        self.year = year
        self.task_num = task_num

        self.solve_module = import_module(f'y{self.year}.t{self.task_num}.solution')
        self.solve_func = vars(self.solve_module)['main']
        self.mode = self.detect_run_mode()

        self.is_test_now = False
        self.expected_answers_for_tests = []
        self.actual_answers_for_tests = []
        self.tests_passed = []
        self.run_results = {
            'parts': {
                part_num: {
                    'test': {

                    },
                    'solution': {

                    }
                } for part_num in [1, 2]
            },
            'last_part_num': None
        }

    def run(self):
        print(f'===== AoC-{self.year}. Task #{self.task_num} =====\n')

        for i, test_input in enumerate(self.get_tests_inputs()):
            self.run_test(test_input, test_num=i + 1)

        self.run_solution()

        if (part_num := self.run_results['last_part_num']) is not None:
            if self.is_autosubmit_allowed(part_num) and self.is_success_tests_for_part(part_num):
                self.submit_answer(part_num)

    def detect_run_mode(self):
        """Get run mode depending on presence of `s` or `t` argument in the solve function.
        This is done to speed up switching between running tests and solution.
        """
        spec = inspect.getfullargspec(self.solve_func).args
        if 's' in spec:
            return self.RunModes.SOLUTION_ONLY
        elif 't' in spec:
            return self.RunModes.TEST_ONLY
        else:
            return self.RunModes.SOLUTION_TEST

    def run_test(self, test_input, test_num):
        if self.mode == self.RunModes.SOLUTION_ONLY:
            return

        self.is_test_now = True

        try:
            self._run_solve_func({
                'read': self.read_mock(test_input),
                'p1': lambda answer: self.print_mock(answer, part_num=1, test_num=test_num),
                'p2': lambda answer: self.print_mock(answer, part_num=2, test_num=test_num),
            })
        except Exception:
            # Re-raise an exception when running tests only
            if self.mode == self.RunModes.TEST_ONLY:
                raise

            # Otherwise, just print it
            print(f'Test #{test_num} raised an exception')

        self.check_test_results(test_num)

        self.is_test_now = False

    def run_solution(self):
        if self.mode == self.RunModes.TEST_ONLY:
            return

        if not self.get_path('input.txt').exists():
            download_input(self.year, self.task_num)

        self._run_solve_func({
            'read': self.read_mock(self.get_input_lines('input.txt')),
            'p1': lambda answer: self.print_mock(answer, part_num=1, test_num=None),
            'p2': lambda answer: self.print_mock(answer, part_num=2, test_num=None),
        })

    def _run_solve_func(self, patches=None):
        if patches:
            for name, value in patches.items():
                self.solve_module.__dict__[name] = value

        kwargs = {
            'is_test': self.is_test_now,
            's': None,
            't': None,
            'autosubmit': None,
            'no_autosubmit': None,
        }
        spec = inspect.getfullargspec(self.solve_func).args
        kwargs = {k: v for k, v in kwargs.items() if k in spec}
        self.solve_func(**kwargs)

    @property
    def verbose(self):
        if self.is_test_now:
            # Print test answer separately only if running test-only mode
            return self.mode == self.RunModes.TEST_ONLY

        return True

    def read_mock(self, return_value):
        def _read(input_type: type = str, group=False):
            if group:
                result = [[input_type(x) for x in group.split('\n')] for group in '\n'.join(return_value).split('\n\n')]
            else:
                result = list(map(input_type, return_value))
            return result

        return _read

    def get_test_passes_for_part(self, part_num):
        return [
            test_passed[part_num - 1]
            for test_passed in self.tests_passed
            if len(test_passed) >= part_num and test_passed[part_num - 1] is not None
        ]

    def is_success_tests_for_part(self, part_num):
        return all(self.get_test_passes_for_part(part_num))

    def print_mock(self, answer, part_num, test_num):
        if self.is_test_now:
            if len(self.actual_answers_for_tests[test_num - 1]) >= part_num:
                self.actual_answers_for_tests[test_num - 1][part_num - 1] = answer
        else:
            test_passes = self.get_test_passes_for_part(part_num)
            info = f'({sum(test_passes)}/{len(test_passes)} tests passed)' if test_passes else ''

            print(f'Part {part_num} answer:', answer, info)
            pyperclip.copy(str(answer))
            self.run_results['last_part_num'] = part_num
            self.run_results['parts'][part_num]['solution']['answer'] = answer

    def check_test_results(self, test_num):
        actual = self.actual_answers_for_tests[test_num - 1]
        expected = self.expected_answers_for_tests[test_num - 1]
        for i, (act, exp) in enumerate(zip(actual, expected)):
            if act is not None and exp is not None:
                act = str(act)
                exp = str(exp)
                is_test_passing = act == exp

                if is_test_passing:
                    self.tests_passed[test_num - 1][i] = True
                    if self.verbose:
                        extra_info = '(OK)'
                    else:
                        continue
                else:
                    self.tests_passed[test_num - 1][i] = False
                    extra_info = f'(expected: {exp})'
            elif act is not None and self.verbose:
                extra_info = '(expected not provided)'
            else:
                continue

            print(f'Test #{test_num}. Part {i + 1} answer: {act} {extra_info}')

    def get_path(self, name):
        return Path(self.solve_module.__file__).parent / name

    def get_input_lines(self, name):
        p = self.get_path(name)
        if p.exists():
            return _read_input(p)

        return None

    def get_tests_inputs(self):
        lines = self.get_input_lines('input_test.txt')

        if lines is None:
            return []

        inputs_raw = re.split(r'\n_+\n', '\n'.join(lines))

        inputs = []
        for input_text in inputs_raw:
            lines, answers = self.get_test_lines_and_answers(input_text)
            self.expected_answers_for_tests.append(answers)
            inputs.append(lines)

        max_answers_for_test = max(len(test_answers) for test_answers in self.expected_answers_for_tests)
        self.expected_answers_for_tests = [
            answers + [None] * (max_answers_for_test - len(answers))
            for answers in self.expected_answers_for_tests
        ]

        self.actual_answers_for_tests = [[None] * max_answers_for_test for _ in inputs]
        self.tests_passed = [[None] * max_answers_for_test for _ in inputs]

        return inputs

    def get_test_lines_and_answers(self, input_text):
        lines = input_text.split('\n')

        # Find expected answers for test
        answers = re.split(r'\n=+\n', '\n'.join(lines))[-1].split('\n')

        # If there are expected answers, remove them from input
        if len(answers) != len(lines):
            answers = [answer if answer != '' else None for answer in answers]
            lines = lines[:-len(answers) - 1]
        else:
            answers = []

        return lines, answers

    def is_autosubmit_allowed(self, part_num):
        """Allow autosubmit, unless there's a _part*_solved file or no_autosubmit flag"""
        spec = inspect.getfullargspec(self.solve_func).args
        if self.get_path(f'_part{part_num}_solved').exists():
            return False
        if 'autosubmit' in spec:
            return True
        if 'no_autosubmit' in spec:
            return False

        return True
        # is_today = datetime.strptime(f'{self.year}/12/{self.task_num}', '%Y/%m/%d').date() == datetime.now().date()
        #
        # return is_today

    def submit_answer(self, part_num):
        answer = self.run_results['parts'][part_num]['solution']['answer']
        print(f'Submitting an answer "{answer}" for part {part_num}...')
        result = submit_answer(self.year, self.task_num, part_num, answer)
        if result['success']:
            with self.get_path(f'_part{part_num}_solved').open('w'):
                pass
            url = f'https://adventofcode.com/{self.year}/day/{self.task_num.lstrip("0")}'
            print(f'Success! Opening URL: {url}.\nResponse: {result["text"]}')
            webbrowser.open(url)
        else:
            print(f'Unsuccessful submit: {result["text"]}')
