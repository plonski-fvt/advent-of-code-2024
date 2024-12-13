def propagate_dict(stones: dict[int, int]) -> dict[int, int]:
    next_stones: dict[int, int] = {}
    for stone, count in stones.items():
        stone_str = str(stone)
        if (stone == 0):
            next_stone_count = next_stones.get(1, 0)
            next_stones[1] = next_stone_count + count
        elif (len(stone_str) % 2) == 0:
            next_stone_a = int(stone_str[:int(len(stone_str)/2)])
            next_stone_b = int(stone_str[int(len(stone_str)/2):])
            next_count_a = next_stones.get(next_stone_a, 0)
            next_stones[next_stone_a] = next_count_a + count
            next_count_b = next_stones.get(next_stone_b, 0)
            next_stones[next_stone_b] = next_count_b + count
        else:
            next_stone = stone * 2024
            next_stone_count = next_stones.get(next_stone, 0)
            next_stones[next_stone] = next_stone_count + count
    return next_stones

file = open("day11-input.txt")

stones = [int(x) for x in file.readline().strip().split()]

stones_dict = {}
for stone in stones:
    current_count = stones_dict.get(stone, 0)
    stones_dict[stone] = current_count + 1

print(stones)
print(len(stones))
print(stones_dict)

for i in range(0, 75, 1):
    print(i + 1)
    stones_dict = propagate_dict(stones_dict)
    print(len(stones_dict))
    print(sum(stones_dict.values()))
