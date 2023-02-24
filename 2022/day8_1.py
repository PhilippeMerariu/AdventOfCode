from typing import List

file = open('input8.txt')
line = file.readline().strip()

grid_size: int = len(line)

grid: List[List[int]] = []
tree_row: List[int] = []

while line:
    for tree in line:
        tree_row.append(int(tree))
    grid.append(tree_row.copy())
    tree_row.clear()
    line = file.readline().strip()
file.close()

visible_trees: int = 0


def is_tree_visible(tree_line: List[int], tree_height: int) -> bool:
    if not tree_line:
        return True
    return max(tree_line) < tree_height


def get_left_tree_line(row: int, col: int) -> List[int]:
    return grid[row][:col]


def get_right_tree_line(row: int, col: int) -> List[int]:
    return grid[row][col+1:]


def get_top_tree_line(row: int, col: int) -> List[int]:
    top_view: List[int] = []
    for t in range(row):
        top_view.append(grid[t][col])
    return top_view


def get_bottom_tree_line(row: int, col: int) -> List[int]:
    bottom_view: List[int] = []
    for t in range(row+1, len(grid)):
        bottom_view.append(grid[t][col])
    return bottom_view


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_tree_visible(get_left_tree_line(i, j), grid[i][j]) or \
                is_tree_visible(get_right_tree_line(i, j), grid[i][j]) or \
                is_tree_visible(get_top_tree_line(i, j), grid[i][j]) or \
                is_tree_visible(get_bottom_tree_line(i, j), grid[i][j]):
            visible_trees += 1
            print(grid[i][j])

print("ANSWER = {0}".format(visible_trees))
