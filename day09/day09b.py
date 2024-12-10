from dataclasses import dataclass

@dataclass
class File:
    position: int
    id: int
    length: int

# modifies the list
def insert_at_first_free_spot(sorted_file_list: list[File], file: File):
    # print("list we are searching: ", sorted_file_list)
    for i in range(len(sorted_file_list) - 1):
        file_before = sorted_file_list[i]
        file_after = sorted_file_list[i+1]
        if (file_before.position + file_before.length + file.length) <= file_after.position:
            file.position = file_before.position + file_before.length
            sorted_file_list = sorted_file_list[:i+1] + [file] + sorted_file_list[i+1:]
            # print("inserting file {} in index {}, position {}".format(file.id, i+1, file.position))
            return sorted_file_list
    # test if there is room before its current location (maintaining ordering)
    file_before = sorted_file_list[-1]
    file_after = file
    if (file_before.position + file_before.length + file.length) <= file_after.position:
        file.position = file_before.position + file_before.length
    return sorted_file_list + [file]

#file = open("day09-test.txt")            
file = open("day09-input.txt")

line = file.readline().strip()

sorted_file_list: list[File] = []

position = 0
next_is_file = True
for c in line:
    if next_is_file:
        sorted_file_list.append(File(position, len(sorted_file_list), int(c)))
        position += int(c)
        next_is_file = False
    else:
        position += int(c)
        next_is_file = True

print(sorted_file_list)

num_files = len(sorted_file_list)

for file_index_to_move in range(num_files - 1, 0, -1):
    # print("file index to move: ", file_index_to_move)
    location_of_file_to_move = next(i for i, x in enumerate(sorted_file_list) if x.id == file_index_to_move)
    file_to_move = sorted_file_list[location_of_file_to_move]
    # print("file to move: ", file_to_move)
    first_part = sorted_file_list[:location_of_file_to_move]
    second_part = sorted_file_list[location_of_file_to_move + 1:]
    first_part = insert_at_first_free_spot(first_part, sorted_file_list[location_of_file_to_move])
    sorted_file_list = first_part + second_part

print(sorted_file_list)

tape = []
position = 0

for file, next_file in zip(sorted_file_list, sorted_file_list[1:]):
    tape = tape + [file.id] * file.length
    tape = tape + [-1] * (next_file.position - (file.position + file.length))

last_file = sorted_file_list[-1]
tape = tape + [last_file.id] * last_file.length

print(tape)

sum = 0
for i, id in enumerate(tape):
    if id >= 0:
        sum += i * id

print(sum)