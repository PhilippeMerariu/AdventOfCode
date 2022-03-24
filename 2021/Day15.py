from typing import List, Dict, Tuple

grid: List[List[int]] = []
risk_levels: Dict[Tuple[int, int], int] = {}

file = open('input15_test.txt')
line = file.readline().strip()

while line:
    grid_line: List[int] = [int(char) for char in line]
    grid.append(grid_line.copy())
    line = file.readline().strip()
file.close()

risk_levels[(0, 0)] = grid[0][0]

all_paths: List[List[Tuple[int, int]]] = [[(0, 0)]]


def add_path(prev_path: List[Tuple[int, int]], new_pos: Tuple[int, int]) -> None:
    new_path: List[Tuple[int, int]] = prev_path
    if len(new_path) >= 2:
        if new_path[-2] == new_pos:
            return
    new_path.append(new_pos)
    all_paths.append(new_path)


while True:
    for path in all_paths.copy():
        x = path[-1][1]
        y = path[-1][0]
        if x < len(grid) - 1:
            add_path(path.copy(), (y, x + 1))
        if y < len(grid) - 1:
            add_path(path.copy(), (y + 1, x))
        if x > 0:
            add_path(path.copy(), (y, x - 1))
        if y > 0:
            add_path(path.copy(), (y - 1, x))
        all_paths.remove(path)

# while True:
#     for (y, x), val in risk_levels.copy().items():
#         if (y, x) == (len(grid) - 1, len(grid) - 1):
#             continue
#         if x < len(grid) - 1:
#             risk_levels.update({(y, x + 1): val + grid[y][x + 1]})
#             print(val + grid[y][x + 1])
#         if y < len(grid) - 1:
#             risk_levels.update({(y + 1, x): val + grid[y + 1][x]})
#             print(val + grid[y + 1][x])
#         risk_levels.pop((y, x))

answer: int = 0
print("ANSWER = {0}".format(answer))
