from abc import ABC, abstractmethod

from utils import read, p1, p2


def main():
    lines = read()

    p1(ObjectInstructionsExecutor(waypoint=(1, 0)).execute(lines).manhattan_dist)
    p2(WaypointInstructionsExecutor(waypoint=(10, 1)).execute(lines).manhattan_dist)


class BaseInstructionsExecutor(ABC):
    """Base class for executing moving instructions."""

    def __init__(self, coords=(0, 0)):
        self.coords = list(coords)

    @property
    def manhattan_dist(self):
        """Return Manhattan distance of the object."""
        return abs(self.coords[0]) + abs(self.coords[1])

    def execute(self, instructions):
        for instruction in instructions:
            command, value = instruction[0], int(instruction[1:])
            self.execute_command(command, value)

        return self

    def change_coords(self, command, value, coords=None):
        """Change coordinates by N/E/W/S command. Use object coordinates by default."""
        if coords is None:
            coords = self.coords

        if command == 'N':
            coords[1] += value
        elif command == 'S':
            coords[1] -= value
        elif command == 'W':
            coords[0] -= value
        elif command == 'E':
            coords[0] += value

    @abstractmethod
    def execute_command(self, command, value):
        pass


class WaypointInstructionsExecutor(BaseInstructionsExecutor):

    def __init__(self, waypoint, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.w_coords = list(waypoint)

    def execute_command(self, command, value):
        if command == 'F':
            self.move_to_waypoint(value)
        elif command in 'NEWS':
            # N/E/W/S commands change waypoint coordinates, not object's ones
            self.change_coords(command, value, coords=self.w_coords)
        elif command in ['L', 'R']:
            self.rotate_waypoint_with_command(command, value)

    def rotate_waypoint_with_command(self, command, value):
        if command == 'L':
            self.rotate_waypoint_cw(degrees=-value)
        elif command == 'R':
            self.rotate_waypoint_cw(degrees=value)

    def rotate_waypoint_cw(self, degrees):
        degrees = degrees % 360

        if degrees == 180:
            self.w_coords = [x * -1 for x in self.w_coords]
        elif degrees == 90:
            self.w_coords = [self.w_coords[1], -self.w_coords[0]]
        elif degrees == 270:
            self.w_coords = [-self.w_coords[1], self.w_coords[0]]

    def move_to_waypoint(self, value):
        self.coords[0] += self.w_coords[0] * value
        self.coords[1] += self.w_coords[1] * value


class ObjectInstructionsExecutor(WaypointInstructionsExecutor):
    """Same as WaypointInstructionsExecutor with the only exception that
    move commands (N/E/W/S) are applied to the object, not the waypoint."""

    def execute_command(self, command, value):
        if command == 'F':
            self.move_to_waypoint(value)
        elif command in 'NEWS':
            self.change_coords(command, value)
        elif command in ['L', 'R']:
            self.rotate_waypoint_with_command(command, value)
