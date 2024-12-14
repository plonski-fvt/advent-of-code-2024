file = open("day12-input.txt")
lines = file.readlines()
map = [[c for c in line.strip()] for line in lines]
rows = len(map)
cols = len(map[0])

def flood_fill(position: tuple[int, int], already_found: set[tuple[int, int]]) -> set[tuple[int, int]]:
    already_found.add((position[0], position[1]))
    symbol = map[position[0]][position[1]]
    neighbor_offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for offset in neighbor_offsets:
        cand_u = position[0] + offset[0]
        cand_v = position[1] + offset[1]
        if cand_u < 0 or cand_u >= rows or cand_v < 0 or cand_v >= cols:
            continue
        if (symbol == map[cand_u][cand_v]) and not (cand_u, cand_v) in already_found:
            already_found = flood_fill((cand_u, cand_v), already_found)
    return already_found

def compute_perimeter(plot_set):
    perimeter = 0
    already_counted = set()
    for pos in plot_set:
        perimeter += 4
        neighbor_offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for offset in neighbor_offsets:
            cand_u = pos[0] + offset[0]
            cand_v = pos[1] + offset[1]
            if (cand_u, cand_v) in already_counted:
                perimeter -= 2
        already_counted.add(pos)
    return perimeter

everything_found = set()
individual_plots: list[tuple[str, set[tuple[int, int]]]]= []

for u in range(rows):
    for v in range(cols):
        if (u, v) in everything_found:
            continue
        plot = (map[u][v], flood_fill((u, v), set()))
        everything_found.update(plot[1])
        individual_plots.append(plot)

print(len(everything_found))
print(len(individual_plots))

cost_sum = 0
for plot in individual_plots:
    area = len(plot[1])
    perimeter = compute_perimeter(plot[1])
    cost_sum += area * perimeter

print(cost_sum)