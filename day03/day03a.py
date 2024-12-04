import re

file = open("day03-input.txt")

lines = file.readlines()
print(len(lines))

sum = 0
for line in lines:
    groups = re.findall(r"mul\((\d+),(\d+)\)", line)
    print(len(groups))
    for group in groups:
        sum += int(group[0]) * int(group[1])

print(sum)
    
