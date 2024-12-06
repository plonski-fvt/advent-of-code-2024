import re
import math

def test_sequence(rules: list[tuple], sequence: list[int]):
    items_in_full_sequence = set(sequence)
    items_previously_in_sequence: set[int] = set()
    for item in sequence:
        for a, b in rules:
            if (item == b) and not (a in items_previously_in_sequence) and (a in items_in_full_sequence):
                return False
        items_previously_in_sequence.add(item)
    return True

#file = open("day05-test.txt")
file = open("day05-input.txt")

rules: list[tuple] = []
rules_complete = False

bad_sequences = []

for line in file:
    if not rules_complete:
        groups = re.match(r"(\d+)\|(\d+)", line)
        if groups is None:
            rules_complete = True
        else:
            rules.append((int(groups[1]), int(groups[2])))
    else:
        sequence = [int(x) for x in line.split(",")]
        if not test_sequence(rules, sequence):
            bad_sequences.append(sequence)

result = 0
for bad_sequence in bad_sequences:
    fixed_sequence = [bad_sequence[0]]
    for i in range(1, len(bad_sequence)):
        for j in range(len(fixed_sequence) + 1):
            candidate_sequence = fixed_sequence[:j] + [bad_sequence[i]] + fixed_sequence[j:]
            # print(candidate_sequence)
            if test_sequence(rules, candidate_sequence):
                fixed_sequence = candidate_sequence
                break
    print(bad_sequence)
    print(fixed_sequence)
    result += fixed_sequence[math.floor(len(fixed_sequence) / 2)]

print(result)
            


    