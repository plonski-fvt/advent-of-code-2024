import re

#file = open("day04-testa.txt")
file = open("day04-input.txt")

lines = file.readlines()

cols = []
for i in range(len(lines[0])):
    cols.append("".join([line[i] for line in lines]))

diags_a_dict = {}
diags_b_dict = {}
for i in range(len(lines)):
    for j in range(len(cols)):
        char = lines[i][j]
        diag_a_index = i - j
        diag_b_index = i + j
        existing_a = diags_a_dict.get(diag_a_index, [])
        existing_b = diags_b_dict.get(diag_b_index, [])
        existing_a.append(char)
        existing_b.append(char)
        diags_a_dict[diag_a_index] = existing_a
        diags_b_dict[diag_b_index] = existing_b

diags_a = ["".join(value) for key, value in diags_a_dict.items()]
diags_b = ["".join(value) for key, value in diags_b_dict.items()]

print(len(lines), len(cols), len(diags_a), len(diags_b))

string_arrays_to_test = [lines, cols, diags_a, diags_b]

count = 0
for array in string_arrays_to_test:
    for line in array:
        matches = re.findall(r"XMAS", line)
        count += len(matches)
        matches = re.findall(r"SAMX", line)
        count += len(matches)

print(count)