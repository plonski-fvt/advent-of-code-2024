# (x, b) describes the output of propagating a stone x, n times
stone_dict: dict[tuple[int, int], list] = {}

def propagate_n_times(stones: list[int], n: int) -> list[int]:
    if n == 1:
        next_stones = []
        for stone in stones:
            stone_str = str(stone)
            if stone == 0:
                next_stones.append(1)
            elif (len(stone_str) % 2) == 0:
                next_stones.append(int(stone_str[:int(len(stone_str)/2)]))
                next_stones.append(int(stone_str[int(len(stone_str)/2):]))
            else:
                next_stones.append(stone * 2024)
        return next_stones
    next_stones_sublists = []
    for stone in stones:
        resultant_stones = stone_dict.get((stone, n), None)
        if resultant_stones is None:
            # n1 = max(1, round(2 * n / 3))
            n1 = 1
            n2 = n - n1
            resultant_stones = propagate_n_times(propagate_n_times([stone], n1), n2)
        next_stones_sublists.append(resultant_stones)
    # print(next_stones_sublists)
    next_stones = [x for xs in next_stones_sublists for x in xs]
    # print(next_stones)
    index = 0
    # this should improve memory efficiency
    for stone, sublist in zip(stones, next_stones_sublists):
        stone_dict[(stone, n)] = next_stones[index:index + len(sublist)]
        index += len(sublist)
    return next_stones

file = open("day11-input.txt")

stones = [int(x) for x in file.readline().strip().split()]

print(stones)
print(len(stones))

for i in range(75):
    print(i + 1)
    resultant_stones = propagate_n_times(stones, i + 1)
    print(len(resultant_stones))
    # print(len(stone_dict))