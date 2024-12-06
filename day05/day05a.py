import re
import math

#file = open("day05-test.txt")
file = open("day05-input.txt")

rules: list[tuple] = []
rules_complete = False


result = 0
for line in file:
    if not rules_complete:
        groups = re.match(r"(\d+)\|(\d+)", line)
        if groups is None:
            rules_complete = True
            print(rules)
        else:
            rules.append((int(groups[1]), int(groups[2])))
    else:
        sequence = [int(x) for x in line.split(",")]
        sequence_is_good = True
        items_previously_in_sequence: set[int] = set()
        for item in sequence:
            for a, b in rules:
                if (item == b) and (a in sequence) and not (a in items_previously_in_sequence):
                    print(item, a, b, sequence)
                    sequence_is_good = False
                    break
            if not sequence_is_good:
                break
            items_previously_in_sequence.add(item)
        if sequence_is_good:
            print(sequence)
            result += sequence[math.floor(len(sequence) / 2)]

print(result)
            


    