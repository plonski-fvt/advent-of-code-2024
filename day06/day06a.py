from dataclasses import dataclass
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass(frozen=True)
class Position:
    row: int
    col: int
    direction: Direction

    def next_position(self):
        offsets = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        offset = offsets[self.direction.value]
        return Position(self.row + offset[0], self.col + offset[1], self.direction)


file = open("day06-input.txt")

lines = file.readlines()

map = [list(line.strip()) for line in lines]
rows = len(map)
cols = len(map[0])

position = None

for i in range(rows):
    for j in range(cols):
        if map[i][j] == "^":
            position = Position(i, j, Direction.UP)

print(position)
assert position is not None

while True:
    map[position.row][position.col] = "X"
    candidate_next_position = position.next_position()
    if (
        (candidate_next_position.row < 0)
        or (candidate_next_position.row >= rows)
        or (candidate_next_position.col < 0)
        or (candidate_next_position.col >= cols)
    ):
        break
    if map[candidate_next_position.row][candidate_next_position.col] == "#":
        next_direction = Direction((candidate_next_position.direction + 1) % 4)
        candidate_next_position = Position(position.row, position.col, next_direction)
    position = candidate_next_position

num_visited = 0
for i in range(rows):
    for j in range(cols):
        if map[i][j] == "X":
            num_visited += 1

print(num_visited)
