import re

file = open("day03-input.txt")

lines = file.readlines()
print(len(lines))

sum = 0
active = True
for line in lines:
    groups = re.findall(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", line)
    print(len(groups))
    for group in groups:
        print(group)
        if len(group[3]) > 0:
            active = True
        elif len(group[4]) > 0:
            active = False
        elif active:
            sum += int(group[1]) * int(group[2])

print(sum)
    
