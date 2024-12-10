file = open("day09-input.txt")

line = file.readline().strip()

positions = []
lengths = []

tape = []

position = 0
next_is_file = True
for c in line:
    if next_is_file:
        tape = tape + [len(positions)] * int(c)
        positions.append(position)
        lengths.append(int(c))
        position += int(c)
        next_is_file = False
    else:
        tape = tape + [-1] * int(c)
        position += int(c)
        next_is_file = True

num_indices = len(positions)
print(len(tape))

final_tape_length = sum(lengths)
print(final_tape_length)

position = 0
for index_to_insert in range(num_indices - 1, 0, -1):
    if position == final_tape_length:
        break
    length_to_insert = lengths[index_to_insert]
    while (position < len(tape)):
        if length_to_insert == 0:
            break
        if tape[position] == -1:
            tape[position] = index_to_insert
            length_to_insert -= 1
        position += 1

final_tape = tape[0:final_tape_length]

sum = 0
for i, id in enumerate(final_tape):
    sum += i * id

print(sum)
    


