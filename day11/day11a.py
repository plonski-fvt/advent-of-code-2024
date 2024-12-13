def propagate(stones: list[int]):
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
            

        

file = open("day11-input.txt")

stones = [int(x) for x in file.readline().strip().split()]

print(stones)
print(len(stones))

for i in range(25):
    stones = propagate(stones)
    print(len(stones))
