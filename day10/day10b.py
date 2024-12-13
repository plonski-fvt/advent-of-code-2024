file = open("day10-input.txt")
lines = file.readlines()
map = [[int(c) for c in line.strip()] for line in lines]
rows = len(map)
cols = len(map[0])

def count_unique_paths(pos: tuple[int, int]) -> int:
    pos_number = map[pos[0]][pos[1]]
    if pos_number == 9:
        return 1
    neighbor_offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    neighbor_positions = [(pos[0] + offset[0], pos[1] + offset[1]) for offset in neighbor_offsets]
    reachable_sum = 0
    for position in neighbor_positions:
        if (position[0] < 0) or (position[0] >= rows) or (position[1] < 0) or (position[1] >= cols):
            continue
        if map[position[0]][position[1]] == pos_number + 1:
            reachable_sum += count_unique_paths(position)
    return reachable_sum

total_sum = 0
for i in range(rows):
    for j in range(cols):
        if map[i][j] == 0:
            reachable_sum = count_unique_paths((i, j))
            print(reachable_sum)
            total_sum += reachable_sum

print(total_sum)