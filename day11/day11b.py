# (x, b) describes the output of propagating a stone x, n times
stone_dict: dict[tuple[int, int], list] = {}

def propagate_n_times(stones: list[int], n: int) -> list[int]:
    next_stones = []
    if n == 1:
        for stone in stones:
            resultant_stones = stone_dict.get((stone, n), None)
            if resultant_stones is None:
                stone_str = str(stone)
                if stone == 0:
                    resultant_stones = [1]
                elif (len(stone_str) % 2) == 0:
                    resultant_stones = [int(stone_str[:int(len(stone_str)/2)]),
                                        int(stone_str[int(len(stone_str)/2):])]
                else:
                    resultant_stones = [stone * 2024]
                stone_dict[(stone, n)] = resultant_stones
            next_stones = next_stones + resultant_stones
        return next_stones
    for stone in stones:
        resultant_stones = stone_dict.get((stone, n), None)
        if resultant_stones is None:
            resultant_stones = propagate_n_times(propagate_n_times([stone], 1), n - 1)
            stone_dict[(stone, n)] = resultant_stones
        next_stones = next_stones + resultant_stones
    return next_stones

file = open("day11-input.txt")

stones = [int(x) for x in file.readline().strip().split()]

print(stones)
print(len(stones))

for i in range(75):
    print(i + 1)
    resultant_stones = propagate_n_times(stones, i + 1)
    print(len(resultant_stones))
    print(len(stone_dict))