from itertools import product

import numpy as np

from utils import read, p1, p2


def main():
    init_state = np.array([list(line) for line in read()]) == "#"
    p1(ConwayCubes(init_state, dimensions=3).run(num_cycles=6).active_num)
    p2(ConwayCubes(init_state, dimensions=4).run(num_cycles=6).active_num)


class ConwayCubes:

    def __init__(self, init_state: np.ndarray, dimensions: int):
        shape = init_state.shape
        new_shape = [1] * (dimensions - len(shape)) + list(shape)
        self.init_state = np.reshape(init_state, tuple(new_shape))
        self.state = self.init_state
        self.dims = dimensions

    def run(self, num_cycles: int):
        prev_state = self.state
        for _cycle_num in range(num_cycles):
            next_state = self.get_next_state(prev_state)
            next_state = self.trim_state(next_state)
            prev_state = next_state
            print(f"{self.dims}-D cycle #{_cycle_num + 1} finished.")
            # self.print_state(next_state)

        self.state = prev_state

        return self

    @property
    def active_num(self):
        return np.sum(self.state)

    def get_next_state(self, prev_state):
        prev_state = np.pad(prev_state, pad_width=1, constant_values=False)
        active_neighbors = np.zeros(shape=prev_state.shape)

        for idx in np.ndindex(prev_state.shape):
            if not prev_state[idx]:
                continue

            for offset in product([-1, 0, 1], repeat=self.dims):
                if all(i == 0 for i in offset):
                    continue

                oidx = tuple(np.array(idx) + np.array(offset))

                # Ignore out-of-bound indices
                if not all(0 <= oidx[i] < prev_state.shape[i] for i in range(self.dims)):
                    continue

                active_neighbors[oidx] += 1

        # Next state is active if:
        # - was active in previous state and had 2 or 3 active neighbors
        # - was inactive in previous state and exactly 3 active neighbors
        return (
            (prev_state & ((active_neighbors == 3) | (active_neighbors == 2)))
            |
            (~prev_state & (active_neighbors == 3))
        )

    def trim_state(self, state):
        for d in range(len(state.shape)):
            slice_start = self.get_empty_edge_size(state, d)
            slice_end = state.shape[d] - self.get_empty_edge_size(state, d, reverse=True)
            state = slice_dim(state, d, slice_=slice(slice_start, slice_end))

        return state

    def get_empty_edge_size(self, state, dimension, reverse=False):
        it = range(state.shape[dimension])
        if reverse:
            it = reversed(it)

        c = 0
        for i in it:
            if not np.any(slice_dim(state, dimension, slice_=i)):
                c += 1
            else:
                break
        return c

    def print_state(self, state):
        for i in range(state.shape[0]):
            print("\n".join("".join("#" if s else "." for s in line) for line in state[i]))
            print()


def slice_dim(arr, dim, slice_):
    idx = [slice(None)] * dim + [slice_]
    return arr[tuple(idx)]
