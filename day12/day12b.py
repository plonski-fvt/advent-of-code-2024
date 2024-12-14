from dataclasses import dataclass, replace

# file = open("day12-test.txt")
file = open("day12-input.txt")
lines = file.readlines()
map = [[c for c in line.strip()] for line in lines]
rows = len(map)
cols = len(map[0])

def map_safe_get(pos: tuple[int, int]):
    if pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols:
        return "OOB"
    return map[pos[0]][pos[1]]

def flood_fill(
    position: tuple[int, int], already_found: set[tuple[int, int]]
) -> set[tuple[int, int]]:
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


@dataclass(frozen=True, eq=True)
class FencePiece:
    pos_upper_left: tuple[int, int]
    vertical: bool
    length: int

    def can_merge(self, other):
        if not self.vertical == other.vertical:
            return False
        # without loss of generality, self will be the upper or left piece that gets merged
        if self.vertical:
            # test that we're not crossing between two holes

            if not (
                (
                    map_safe_get((self.pos_upper_left[0] + self.length - 1, 
                                  self.pos_upper_left[1]))
                    == map_safe_get((self.pos_upper_left[0] + self.length, 
                                  self.pos_upper_left[1]))
                )
                or (
                    map_safe_get((self.pos_upper_left[0] + self.length - 1, 
                                  self.pos_upper_left[1] + 1))
                    == map_safe_get((self.pos_upper_left[0] + self.length, 
                                  self.pos_upper_left[1] + 1))
                )
            ):
                return False
            return (
                self.pos_upper_left[0] + self.length == other.pos_upper_left[0]
            ) and (self.pos_upper_left[1] == other.pos_upper_left[1])
        else:
            if not (
                (
                    map_safe_get((self.pos_upper_left[0], 
                                  self.pos_upper_left[1] + self.length - 1))
                    == map_safe_get((self.pos_upper_left[0], 
                                     self.pos_upper_left[1] + self.length))
                )
                or (
                    map_safe_get((self.pos_upper_left[0] + 1, 
                                  self.pos_upper_left[1] + self.length - 1))
                    == map_safe_get((self.pos_upper_left[0] + 1, 
                                     self.pos_upper_left[1] + self.length))
                )
            ):
                return False
            return (self.pos_upper_left[0] == other.pos_upper_left[0]) and (
                self.pos_upper_left[1] + self.length == other.pos_upper_left[1]
            )


def compute_raw_fence_pieces(plot_set: set[tuple[int, int]]):
    fence_piece_set: set[FencePiece] = set()
    for pos in plot_set:
        fence_pieces = [
            FencePiece(pos, True, 1),
            FencePiece(pos, False, 1),
            FencePiece((pos[0] - 1, pos[1]), False, 1),
            FencePiece((pos[0], pos[1] - 1), True, 1),
        ]
        for piece in fence_pieces:
            if piece in fence_piece_set:
                fence_piece_set.remove(piece)
            else:
                fence_piece_set.add(piece)
    return fence_piece_set


def merge_fence_pieces(fence_piece_set: set[FencePiece]):
    found_merge = True
    while found_merge:
        found_merge = False
        for piece_a in fence_piece_set:
            for piece_b in fence_piece_set:
                if piece_a.can_merge(piece_b):
                    found_merge = True
                    fence_piece_set.remove(piece_a)
                    fence_piece_set.remove(piece_b)
                    new_length = piece_a.length + piece_b.length
                    new_piece = replace(piece_a, length=new_length)
                    fence_piece_set.add(new_piece)
                    break
            if found_merge:
                break
    return fence_piece_set


everything_found = set()
individual_plots: list[tuple[str, set[tuple[int, int]]]] = []

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
    fence_piece_set = compute_raw_fence_pieces(plot[1])
    print(plot[0], area)
    print(len(fence_piece_set))
    print(fence_piece_set)
    fence_piece_set = merge_fence_pieces(fence_piece_set)
    print(len(fence_piece_set))
    print(fence_piece_set)
    cost_sum += area * len(fence_piece_set)

print(cost_sum)
