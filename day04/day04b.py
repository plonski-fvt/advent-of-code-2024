import re

templates = [r"M.S.A.M.S", r"S.S.A.M.M", r"M.M.A.S.S", r"S.M.A.S.M"]

file = open("day04-input.txt")

lines = file.readlines()
num_cols = len(lines[0])

result = 0
for i in range(len(lines) - 2):
    for j in range(num_cols - 3):
        row0 = lines[i][j:j+3]
        row1 = lines[i+1][j:j+3]
        row2 = lines[i+2][j:j+3]
        patch = row0 + row1 + row2
        for template in templates:
            if re.match(template, patch) is not None:
                result += 1

print(result)