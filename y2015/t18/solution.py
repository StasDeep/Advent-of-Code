from itertools import product

import numpy as np

from utils import read, p1, p2
from y2020.t17.solution import ConwayCubes


class StuckConwayCubes(ConwayCubes):

    def run(self, num_cycles: int):
        prev_state = self.state

        for corner in product([0, -1], repeat=2):
            prev_state[corner] = True

        for _cycle_num in range(num_cycles):
            next_state = self.get_next_state(prev_state)
            prev_state = next_state

            for corner in product([0, -1], repeat=2):
                prev_state[corner] = True

        self.state = prev_state
        return self


def main(s):
    init_state = np.array([list(line) for line in read()]) == "#"
    p1(ConwayCubes(init_state, dimensions=2, pad=False).run(num_cycles=100).active_num)
    p2(StuckConwayCubes(init_state, dimensions=2, pad=False).run(num_cycles=100).active_num)
