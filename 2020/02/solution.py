from abc import ABC, abstractmethod

from utils import read, p1, p2


class BasePolicy(ABC):

    def __init__(self, letter, lower, upper):
        self.letter = letter
        self.lower = lower
        self.upper = upper

    @classmethod
    def is_valid_from_test_string(cls, test_string):
        policy, pswd = test_string.split(": ")
        borders, letter = policy.split(" ")
        lower, upper = map(int, borders.split("-"))
        policy = cls(letter, lower, upper)
        return policy.is_valid(pswd)

    @abstractmethod
    def is_valid(self, pswd):
        pass


class LetterCountRangePolicy(BasePolicy):

    def is_valid(self, pswd):
        return self.lower <= pswd.count(self.letter) <= self.upper


class XorMatchPolicy(BasePolicy):

    def is_valid(self, pswd):
        first_match = pswd[self.lower - 1] == self.letter
        second_match = pswd[self.upper - 1] == self.letter
        return sum([first_match, second_match]) == 1


def main():
    lines = read()

    p1(sum(LetterCountRangePolicy.is_valid_from_test_string(line) for line in lines))
    p2(sum(XorMatchPolicy.is_valid_from_test_string(line) for line in lines))


if __name__ == '__main__':
    main()
