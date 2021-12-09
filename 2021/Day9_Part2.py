from typing import List, Tuple

file = open('input9.txt')
line = file.readline().strip()

cave_map: List[str] = []
basins: List[int] = []
locations_passed: List[Tuple[int, int]] = []

while line:
    cave_map.append(line)
    line = file.readline().strip()
file.close()


def get_adjacent(row: int, col: int, height: int, width: int) -> List[int]:
    adjacent: List[int] = []
    if row > 0 and (row - 1, col) not in locations_passed:
        adjacent.append(int(cave_map[row - 1][col]))  # top
        if cave_map[row - 1][col] != '9':
            locations_passed.append((row - 1, col))
    if row < height and (row + 1, col) not in locations_passed:
        adjacent.append(int(cave_map[row + 1][col]))  # bottom
        if cave_map[row + 1][col] != '9':
            locations_passed.append((row + 1, col))
    if col > 0 and (row, col - 1) not in locations_passed:
        adjacent.append(int(cave_map[row][col - 1]))  # left
        if cave_map[row][col - 1] != '9':
            locations_passed.append((row, col - 1))
    if col < width and (row, col + 1) not in locations_passed:
        adjacent.append(int(cave_map[row][col + 1]))  # right
        if cave_map[row][col + 1] != '9':
            locations_passed.append((row, col + 1))
    return adjacent


def get_basin(row: int, col: int, height: int, width: int) -> int:
    basin_size: int = 1
    locations_passed.append((row, col))
    for location in locations_passed:
        adj = get_adjacent(location[0], location[1], height, width)
        basin_size += len([x for x in adj if x != 9])
    return basin_size


for i in range(len(cave_map)):
    for j in range(len(cave_map[i])):
        current: int = int(cave_map[i][j])
        if current == 9:
            continue
        if (i, j) not in locations_passed:
            basins.append(get_basin(i, j, len(cave_map)-1, len(cave_map[i])-1))

answer: int = 1

for i in range(3):
    answer *= max(basins)
    basins.remove(max(basins))

print("ANSWER = {0}".format(answer))
