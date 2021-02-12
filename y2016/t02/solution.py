from abc import ABC, abstractmethod
from itertools import product

from utils import read, p1, p2


def main():
    lines = read()

    p1(SimplePINFinder(lines).find_pin())
    p2(DiamondPINFinder(lines, start_pos=(-2+0j)).find_pin())


class BasePINFinder(ABC):

    moves_map = {"U": +1j, "D": -1j, "L": -1, "R": +1}

    def __init__(self, instructions, start_pos=0 + 0j):
        self.instructions = instructions
        self.cur_pos = start_pos

    def find_pin(self):
        code = ""
        for instruction in self.instructions:
            for move in instruction:
                if self.is_valid_pos(next_pos := self.cur_pos + self.moves_map[move]):
                    self.cur_pos = next_pos

            code += self.code_from_pos(self.cur_pos)

        return code

    @abstractmethod
    def code_from_pos(self, pos):
        ...

    @abstractmethod
    def is_valid_pos(self, pos):
        ...


class SimplePINFinder(BasePINFinder):

    def code_from_pos(self, pos):
        return str(round(5 + pos.real - pos.imag * 3))

    def is_valid_pos(self, pos):
        return all(round(abs(coef)) <= 1 for coef in [pos.real, pos.imag])


class DiamondPINFinder(BasePINFinder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sorted_positions = sorted(
            [complex(x, y) for x, y in product(range(-2, 3), repeat=2) if abs(x) + abs(y) <= 2],
            key=lambda c: (c.imag, -c.real),
            reverse=True
        )

    def code_from_pos(self, pos):
        return "123456789ABCD"[self.sorted_positions.index(pos)]

    def is_valid_pos(self, pos):
        return pos in self.sorted_positions
