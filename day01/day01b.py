import re

file = open("day01-input.txt")

list_a = []
list_b = []

for line in file:
    # print(line)
    match = re.match(r"(\d+)\s+(\d+)", line)
    if match is not None:
        groups = match.groups()
        list_a.append(int(groups[0]))
        list_b.append(int(groups[1]))
    # print(list_a)
    # print(list_b)

list_a.sort()
list_b.sort()

sim_scores = [a * list_b.count(a) for a in list_a]
total_sim_score = sum(sim_scores)

print(total_sim_score)