import re
from copy import copy
from dataclasses import dataclass
from functools import total_ordering, lru_cache
from itertools import combinations
from typing import List, Iterable

from utils import read, p1, p2


def main(t):
    lines = read()

    facility = Facility()
    for line in lines:
        items = re.findall(r'([a-z-]+ (?:microchip|generator))', line)
        facility.add_floor([pair_part_from_string(i) for i in items])

    p1(facility.find_best_moves_num())

    # new_parts = [
    #     Generator('elerium'),
    #     Microchip('elerium'),
    #     Generator('dilithium'),
    #     Microchip('dilithium'),
    # ]
    # facility.floors[0].parts.extend(new_parts)
    # facility._all_items.extend(new_parts)
    # facility._all_items.sort()
    # p2(facility.find_best_moves_num())


def pair_part_from_string(text):
    if 'generator' in text:
        return Generator(elem=text.split()[0])
    elif 'microchip' in text:
        return Microchip(elem=text.split('-')[0])
    else:
        raise ValueError(f'Unknown part: {text}')


@total_ordering
@dataclass
class PairPart:
    elem: str

    def is_compatible(self, other: 'PairPart'):
        return self.elem == other.elem

    def __repr__(self):
        return f'<{self.elem[:2].title()}{type(self).__name__[0]}>'

    def __lt__(self, other):
        return repr(self) < repr(other)

    def __eq__(self, other):
        return repr(self) == repr(other)


class Generator(PairPart):
    pass


class Microchip(PairPart):
    pass


@dataclass
class Floor:
    parts: List[PairPart]

    def __contains__(self, item):
        return item in self.parts

    def is_safe(self):
        chips = [part for part in self.parts if isinstance(part, Microchip)]
        gens = [part for part in self.parts if isinstance(part, Generator)]
        for chip in chips:
            if not any(chip.is_compatible(gen) for gen in gens) and gens:
                return False
        return True

    def add(self, parts: Iterable[PairPart]):
        for part in parts:
            self.parts.append(part)

    def remove(self, parts: Iterable[PairPart]):
        for part in parts:
            self.parts.remove(part)

    def __copy__(self):
        return Floor(copy(self.parts))


class Facility:

    def __init__(self):
        self.floors: List[Floor] = []
        self.elevator_floor = 0

        self._all_items = []

    def add_floor(self, items: List[PairPart]):
        self.floors.append(Floor(items))
        self._all_items.extend(items)
        self._all_items.sort()

    @property
    def state(self):
        lines = []
        for i, floor in enumerate(reversed(self.floors)):
            floor_num = len(self.floors) - i
            is_elev = self.elevator_floor == floor_num - 1

            items_strings = []
            for item in self._all_items:
                if item in floor:
                    items_strings.append(repr(item)[1:-1])
                else:
                    items_strings.append(' . ')
            items_str = ' '.join(items_strings)

            lines.append(f'F{floor_num}  {"E" if is_elev else "."} {items_str}')

        return lines

    @property
    def state_str(self):
        return '\n'.join(self.state)

    @property
    @lru_cache
    def memo_state(self):
        # return self.state_str
        i = 0
        names = {}
        s = f'{self.elevator_floor},'
        for floor in self.floors:
            for part in sorted(floor.parts, key=lambda x: names.get(x.elem, 1000)):
                if part.elem not in names:
                    names[part.elem] = i
                    i += 1
                s += f'{names[part.elem]}{part.__class__.__name__[0]}'
            s += '|'
        return s

    def print_state(self):
        print(self.state_str)

    def is_safe(self):
        return all(floor.is_safe() for floor in self.floors)

    def is_moved_to_last(self):
        return all(item in self.floors[-1] for item in self._all_items)

    def new_facility(self, elevator, comb):
        f = Facility()
        f._all_items = self._all_items
        f.floors = [copy(floor) for floor in self.floors]

        f.elevator_floor = elevator
        f.floors[self.elevator_floor].remove(comb)
        f.floors[elevator].add(comb)
        return f

    def find_next_states(self):
        for move in [+1, -1]:
            elevator = self.elevator_floor + move

            # Ignore elevator moves to wrong floors
            if elevator < 0 or elevator >= len(self.floors):
                continue

            # Ignore moving to the F1 if it's empty
            if not self.floors[0].parts and self.elevator_floor == 1 and move == -1:
                continue

            # Ignore moving to the F2 if F1 and F2 are empty
            if not self.floors[0].parts and not self.floors[1].parts and self.elevator_floor == 2 and move == -1:
                continue

            parts = self.floors[self.elevator_floor].parts

            if move == +1:
                # Don't move one up, if can move two items up
                facs_with_2 = self.get_new_facilities(elevator, parts, num_to_take=2)
                yield from facs_with_2

                if not facs_with_2:
                    yield from self.get_new_facilities(elevator, parts, num_to_take=1)
            else:
                # Don't move two down, if can move one item down
                facs_with_1 = self.get_new_facilities(elevator, parts, num_to_take=1)
                yield from facs_with_1

                if not facs_with_1:
                    yield from self.get_new_facilities(elevator, parts, num_to_take=2)

    def get_new_facilities(self, elevator, parts, num_to_take):
        facs = []
        for comb in combinations(parts, num_to_take):
            next_fac = self.new_facility(elevator, comb)

            # Ignore unsafe steps
            if not next_fac.is_safe():
                continue

            facs.append(next_fac)

        return facs

    def find_best_moves_num(self):
        steps_memo = {self.memo_state: 0}
        queue = [self]
        queue_set = {self.memo_state}

        i = 0

        while queue:
            i += 1
            cur_fac = queue.pop(0)
            queue_set.remove(cur_fac.memo_state)

            for next_fac in cur_fac.find_next_states():
                # Ignore visited states
                if next_fac.memo_state in steps_memo:
                    continue

                # Ignore states already in the queue
                if next_fac.memo_state in queue_set:
                    continue

                steps_num = steps_memo[cur_fac.memo_state] + 1
                # print(f'Steps made: {steps_num}')
                # next_fac.print_state()
                # print(next_fac.memo_state)
                # print()

                queue.append(next_fac)
                queue_set.add(next_fac.memo_state)
                steps_memo[next_fac.memo_state] = steps_num

                if next_fac.is_moved_to_last():
                    print(f'Total iterations: {i}')
                    return steps_num
