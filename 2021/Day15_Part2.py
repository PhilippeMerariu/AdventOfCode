import copy
import sys
from typing import List, Tuple

grid: List[List[int]] = []
shortest_path: List[List[bool]] = []
distances: List[List[int]] = []

file = open('input15.txt')
line = file.readline().strip()

while line:
    grid_line: List[int] = [int(char) for char in line]
    grid.append(grid_line.copy())
    line = file.readline().strip()
file.close()

new_grid_size: int = len(grid) * 5

# add extension to rows
for gl in grid.copy():
    for val in gl:
        if len(gl) == new_grid_size:
            break
        if val == 9:
            gl.append(1)
        else:
            gl.append(val + 1)

# add extension to columns
incremented_grid: List[List[int]] = copy.deepcopy(grid)
while len(grid) < new_grid_size:
    for i in range(len(incremented_grid)):
        for j in range(len(incremented_grid[i])):
            value: int = incremented_grid[i][j]
            if value == 9:
                incremented_grid[i][j] = 1
            else:
                incremented_grid[i][j] += 1

    for inc_grid_row in incremented_grid:
        grid.append(inc_grid_row.copy())

for i in range(len(grid)):
    shortest_path_row: List[bool] = []
    distances_row: List[int] = []
    for j in range(len(grid)):
        shortest_path_row.append(False)
        distances_row.append(sys.maxsize)
    shortest_path.append(shortest_path_row.copy())
    distances.append(distances_row.copy())
distances[0][0] = 0
last_index: int = len(grid) - 1


def find_adjacent(x: int, y: int) -> List[Tuple[int, int]]:
    adjacent: List[Tuple[int, int]] = []
    if x < last_index:  # check right
        adjacent.append((y, x + 1))
    if y < last_index:  # check down
        adjacent.append((y + 1, x))
    if x > 0:  # check left
        adjacent.append((y, x - 1))
    if y > 0:  # check up
        adjacent.append((y - 1, x))
    return adjacent


def calculate_adjacent_distances(x: int, y: int) -> None:
    adjacent: List[Tuple[int, int]] = find_adjacent(x, y)
    for i, j in adjacent:
        if shortest_path[i][j] is False:
            cost: int = distances[y][x] + grid[i][j]
            distances[i][j] = min(cost, distances[i][j])


def find_min_cost() -> Tuple[int, int]:
    min_dist: int = sys.maxsize
    min_dist_pos: Tuple[int, int] = (-1, -1)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if distances[i][j] < min_dist and shortest_path[i][j] is False:
                min_dist = distances[i][j]
                min_dist_pos = (i, j)

    return min_dist_pos


nb_of_elements: int = pow(len(grid), 2)
count: int = 0
while not shortest_path[last_index][last_index]:
    y, x = find_min_cost()
    shortest_path[y][x] = True
    calculate_adjacent_distances(x, y)
    if count % 1000 == 0:
        print("{0} of {1}".format(count, nb_of_elements))
    count += 1

answer: int = distances[last_index][last_index]
print("ANSWER = {0}".format(answer))
