import re

# file = open("day08-test.txt")
file = open("day08-input.txt")

lines = file.readlines()
rows = len(lines)
cols = len(lines[0].strip())

antenna_location_lists: dict[str, list[tuple[int, int]]] = {}

for i in range(rows):
    for match in re.finditer(r"\d|\w", lines[i]):
        location_list = antenna_location_lists.get(match.group(), [])
        location_list.append((i, match.start()))
        antenna_location_lists[match.group()] = location_list

print(antenna_location_lists)

antinode_locations = set()

for key, location_list in antenna_location_lists.items():
    for location_a in location_list:
        for location_b in location_list:
            if location_a == location_b:
                continue
            row_diff = location_b[0] - location_a[0]
            col_diff = location_b[1] - location_a[1]
            # this is a very loose upper bound
            for i in range(rows + cols):
                antinode_location = (
                    location_a[0] + i * row_diff,
                    location_a[1] + i * col_diff,
                )
                antinode_locations.add(antinode_location)

print(antinode_locations)

num_valid_locations = 0
for location in antinode_locations:
    if (
        (location[0] >= 0)
        and (location[0] < rows)
        and (location[1] >= 0)
        and (location[1] < cols)
    ):
        num_valid_locations += 1

print(num_valid_locations)
