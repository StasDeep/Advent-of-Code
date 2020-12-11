from abc import ABC, abstractmethod
from copy import deepcopy

from utils import read, p1, p2


class BaseGameOfSeat(ABC):

    def __init__(self, lines):
        self.initial_state = [list(line) for line in lines]
        self.height = len(self.initial_state)
        self.width = len(self.initial_state[0])
        self.last_state = None

    @abstractmethod
    def is_to_be_occupied(self, i, j):
        pass

    @abstractmethod
    def is_to_be_freed(self, i, j):
        pass

    def play(self, print_states=False):
        self.last_state = deepcopy(self.initial_state)

        while True:
            next_state = deepcopy(self.last_state)
            changed = False
            for i in range(self.height):
                for j in range(self.width):
                    if self.last_state[i][j] == 'L':
                        if self.is_to_be_occupied(i, j):
                            next_state[i][j] = '#'
                            changed = True
                    elif self.last_state[i][j] == '#':
                        if self.is_to_be_freed(i, j):
                            next_state[i][j] = 'L'
                            changed = True

            if print_states:
                for line in next_state:
                    print(''.join(line))
                print()

            self.last_state = next_state

            if not changed:
                break

        return self

    def is_inside(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    @property
    def occupied_count(self):
        return sum(line.count('#') for line in self.last_state)


class GameOfAdjacentSeat(BaseGameOfSeat):

    def is_to_be_occupied(self, i, j):
        return self.find_adj_occup(i, j) == 0

    def is_to_be_freed(self, i, j):
        return self.find_adj_occup(i, j) >= 4

    def find_adj_occup(self, i, j):
        occup_adj = 0
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if m == 0 and n == 0:
                    continue
                idxi = i + m
                idxj = j + n
                if not self.is_inside(idxi, idxj):
                    continue
                if self.last_state[idxi][idxj] == '#':
                    occup_adj += 1
        return occup_adj


class GameOfSeenSeat(BaseGameOfSeat):

    def is_to_be_occupied(self, i, j):
        return self.find_seen_occup(i, j) == 0

    def is_to_be_freed(self, i, j):
        return self.find_seen_occup(i, j) >= 5

    def find_seen_occup(self, i, j):
        max_multiplier = max(self.height, self.width)

        occup_c = 0
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if m == 0 and n == 0:
                    continue

                for multiplier in range(1, max_multiplier):
                    idxi = i + m * multiplier
                    idxj = j + n * multiplier

                    if not self.is_inside(idxi, idxj):
                        break

                    if self.last_state[idxi][idxj] == 'L':
                        break

                    if self.last_state[idxi][idxj] == '#':
                        occup_c += 1
                        break
        return occup_c


def main():
    lines = read()

    p1(GameOfAdjacentSeat(lines).play().occupied_count)
    p2(GameOfSeenSeat(lines).play().occupied_count)
