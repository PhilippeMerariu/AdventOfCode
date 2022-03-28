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
deleted_paths: List[List[Tuple[int, int]]] = []
current_best: int = -1


def add_path(prev_path: List[Tuple[int, int]], new_pos: Tuple[int, int]) -> None:
    global current_best
    new_path: List[Tuple[int, int]] = prev_path
    if new_pos in new_path:
        return
    new_path.append(new_pos)
    if new_path in deleted_paths or new_path in all_paths:
        return
    if calculate_path_cost(new_path) > current_best > 0:
        deleted_paths.append(new_path)
        return
    if new_pos == (last_index, last_index):
        if calculate_path_cost(new_path) <= current_best < 0:
            current_best = calculate_path_cost(new_path)
        else:
            deleted_paths.append(new_path)
            return
    all_paths.append(new_path)



def calculate_path_cost(path: List[Tuple[int, int]]) -> int:
    cost: int = 0
    for (y, x) in path:
        cost += grid[y][x]
    return cost


last_index: int = len(grid) - 1

# Start with the simplest paths (along the borders)
top_and_right_border: List[Tuple[int, int]] = []
left_and_bottom_border: List[Tuple[int, int]] = []
for i in range(len(grid)):
    top_and_right_border.append((0, i))
    left_and_bottom_border.append((i, 0))
for i in range(len(grid)):
    top_and_right_border.append((i, last_index))
    left_and_bottom_border.append((last_index, i))
all_paths.append(top_and_right_border)
all_paths.append(left_and_bottom_border)

while not all((p[-1][0], p[-1][1]) == (last_index, last_index) for p in all_paths):
    for path in all_paths.copy():
        # remove paths that are already costlier than the current best path
        if calculate_path_cost(path) > current_best > 0:
            all_paths.remove(path)
            deleted_paths.append(path)
            continue
        x = path[-1][1]
        y = path[-1][0]
        if (x, y) == (last_index, last_index):
            path_cost: int = calculate_path_cost(path)
            if path_cost <= current_best or current_best == -1:
                current_best = path_cost
            else:
                all_paths.remove(path)
                deleted_paths.append(path)
            continue
        if x < last_index:  # move right
            add_path(path.copy(), (y, x + 1))
        if y < last_index:  # move down
            add_path(path.copy(), (y + 1, x))
        # if x > 0:  # move left
        #     add_path(path.copy(), (y, x - 1))
        # if y > 0:  # move up
        #     add_path(path.copy(), (y - 1, x))
        try:
            all_paths.remove(path)
            deleted_paths.append(path)
        except ValueError:
            pass  # skip removal of invalid path

answer: int = current_best
print("ANSWER = {0}".format(answer))
