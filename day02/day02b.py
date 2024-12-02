def test_safety(levels):
    increasing = levels[1] > levels[0]
    for level, next_level in zip(levels, levels[1:]):
        safe = False
        if abs(level - next_level) < 1:
            break
        if abs(level - next_level) > 3:
            break
        if increasing:
            if level >= next_level:
                break
        else:
            if level <= next_level:
                break
        safe = True
    return safe


file = open("day02-input.txt")

num_safe = 0

for line in file:
    levels = [int(x) for x in line.split()]
    base_safe = test_safety(levels)
    if base_safe:
        num_safe += 1
        continue

    for i in range(len(levels)):
        modified_level = levels[0:i] + levels[i+1:]
        modified_safe = test_safety(modified_level)
        if modified_safe:
            num_safe +=1
            break

print(num_safe)