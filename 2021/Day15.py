import sys
from typing import List, Dict, Tuple

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


for _ in range(pow(len(grid), 2)):
    y, x = find_min_cost()
    shortest_path[y][x] = True
    calculate_adjacent_distances(x, y)


answer: int = distances[last_index][last_index]
print("ANSWER = {0}".format(answer))
