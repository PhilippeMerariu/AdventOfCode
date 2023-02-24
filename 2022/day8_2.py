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
max_scenic_score: int = -1


def tree_view(tree_line: List[int], tree_height: int) -> int:
    nb_trees: int = 0
    for height in tree_line:
        nb_trees += 1
        if height >= tree_height:
            break
    return nb_trees


def get_left_tree_line(row: int, col: int) -> List[int]:
    left_view: List[int] = grid[row][:col]
    left_view.reverse()
    return left_view


def get_right_tree_line(row: int, col: int) -> List[int]:
    return grid[row][col + 1:]


def get_top_tree_line(row: int, col: int) -> List[int]:
    top_view: List[int] = []
    for t in range(row):
        top_view.append(grid[t][col])
    top_view.reverse()
    return top_view


def get_bottom_tree_line(row: int, col: int) -> List[int]:
    bottom_view: List[int] = []
    for t in range(row + 1, len(grid)):
        bottom_view.append(grid[t][col])
    return bottom_view


for i in range(len(grid)):
    for j in range(len(grid[i])):
        left_view_trees: int = tree_view(get_left_tree_line(i, j), grid[i][j])
        right_view_trees: int = tree_view(get_right_tree_line(i, j), grid[i][j])
        top_view_trees: int = tree_view(get_top_tree_line(i, j), grid[i][j])
        bottom_view_trees: int = tree_view(get_bottom_tree_line(i, j), grid[i][j])
        scenic_score: int = left_view_trees * right_view_trees * top_view_trees * bottom_view_trees
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print("ANSWER = {0}".format(max_scenic_score))
