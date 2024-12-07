from dataclasses import dataclass, replace
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass(frozen=True, eq=True)
class Position:
    row: int
    col: int
    direction: Direction

    def next_position(self):
        offsets = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        offset = offsets[self.direction.value]
        return replace(self, row=self.row + offset[0], col=self.col + offset[1])

@dataclass(frozen=True, eq=True)
class Obstacle:
    row: int
    col: int

file = open("day06-input.txt")

lines = file.readlines()

map = [list(line.strip()) for line in lines]
rows = len(map)
cols = len(map[0])

starting_position = None
obstacles = set()

for i in range(rows):
    for j in range(cols):
        if map[i][j] == "^":
            starting_position = Position(i, j, Direction.UP)
        if map[i][j] == "#":
            obstacles.add(Obstacle(i,j))
        

print(starting_position)
assert starting_position is not None

position = replace(starting_position)

trajectory = []

while True:
    trajectory.append(replace(position))
    candidate_next_position = position.next_position()
    if (
        (candidate_next_position.row < 0)
        or (candidate_next_position.row >= rows)
        or (candidate_next_position.col < 0)
        or (candidate_next_position.col >= cols)
    ):
        break
    if Obstacle(candidate_next_position.row, candidate_next_position.col) in obstacles:
        next_direction = Direction((candidate_next_position.direction + 1) % 4)
        candidate_next_position = replace(position, direction=next_direction)
    position = candidate_next_position

print(len(trajectory))

obstacles_we_could_add = set()

for i in range(1, len(trajectory)):
    print(i)
    new_trajectory = set()
    position = starting_position
    new_obstacles = obstacles.copy()
    candidate_obstacle = Obstacle(trajectory[i].row, trajectory[i].col)
    new_obstacles.add(candidate_obstacle)
    while True:
        if position in new_trajectory:
            obstacles_we_could_add.add(candidate_obstacle)
            print(candidate_obstacle)
            print(position)
            break
        new_trajectory.add(replace(position))
        candidate_next_position = position.next_position()
        if (
            (candidate_next_position.row < 0)
            or (candidate_next_position.row >= rows)
            or (candidate_next_position.col < 0)
            or (candidate_next_position.col >= cols)
        ):
            break
        if Obstacle(candidate_next_position.row, candidate_next_position.col) in new_obstacles:
            next_direction = Direction((candidate_next_position.direction + 1) % 4)
            candidate_next_position = replace(position, direction=next_direction)
        position = candidate_next_position

print(len(obstacles_we_could_add))