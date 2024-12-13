import numpy as np

# (x, b) describes the output of propagating a stone x, n times
stone_dict: dict[tuple[int, int], np.ndarray] = {}

def propagate_n_times(stones: np.ndarray, n: int) -> np.ndarray:
    if n == 1:
        next_stones = np.array([])
        for stone in stones:
            stone_str = str(int(stone))
            if stone == 0:
                next_stones = np.append(next_stones, 1)
            elif (len(stone_str) % 2) == 0:
                next_stones = np.append(next_stones, 
                                        np.array([int(stone_str[:int(len(stone_str)/2)]),
                                        int(stone_str[int(len(stone_str)/2):])]))
            else:
                next_stones = np.append(next_stones, stone * 2024)
        return np.array(next_stones)
    next_stones_sublists: list[np.ndarray] = []
    for stone in stones:
        resultant_stones = stone_dict.get((stone, n), None)
        if resultant_stones is None:
            # print("cache miss: {} {}".format(stone, n))
            # n1 = max(1, round(2 * n / 3))
            n1 = 1
            n2 = n - n1
            resultant_stones = propagate_n_times(propagate_n_times(np.array([stone]), n1), n2)
        # else:
            # print("cache hit: {} {}".format(stone, n))
        next_stones_sublists.append(resultant_stones)
    # print(next_stones_sublists)
    next_stones = np.array([x for xs in next_stones_sublists for x in xs])
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
    resultant_stones = propagate_n_times(np.array(stones), i + 1)
    print(len(resultant_stones))
    # print(len(stone_dict))