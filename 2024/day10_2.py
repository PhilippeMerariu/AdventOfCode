file = open('input10.txt')
line = file.readline()

result = 0
map = []
trailheads = []

while line:
    line = line.strip('\n')
    map_row = [x for x in line]
    map.append(map_row.copy())
    line = file.readline()
file.close()

def find_next_paths(pos, path=None):
    possible_paths = []
    prow = pos[0]
    pcol = pos[1]
    nb = int(map[prow][pcol])

    if path is None:
        path=[pos]
    else:
        path = path + [pos]

    if nb == 9:
        return [path]

    if prow > 0 and map[prow - 1][pcol] == str(nb + 1):  # check above
        possible_paths.extend(find_next_paths((prow - 1, pcol), path))
    if prow < len(map) - 1 and map[prow + 1][pcol] == str(nb + 1):  # check below
        possible_paths.extend(find_next_paths((prow + 1, pcol), path))
    if pcol < len(map[prow]) - 1 and map[prow][pcol + 1] == str(nb + 1):  # check left
        possible_paths.extend(find_next_paths((prow, pcol + 1), path))
    if pcol > 0 and map[prow][pcol - 1] == str(nb + 1):  # check right
        possible_paths.extend(find_next_paths((prow, pcol - 1), path))
    return possible_paths

# Find trailheads
for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == '0':
            trailheads.append((row, col))

all_paths = []
for i, th in enumerate(trailheads):
    all_paths.extend(find_next_paths(th))
    print(f"{len(all_paths)} for trailhead #{i + 1}/{len(trailheads)}: {th}")
    result += len(all_paths)
    all_paths.clear()

print(f"ANSWER = {result}")
