file = open("day02-input.txt")

num_safe = 0

for line in file:
    levels = [int(x) for x in line.split()]
    increasing = levels[0] < levels[1]
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
    if safe:
        num_safe += 1

print(num_safe)