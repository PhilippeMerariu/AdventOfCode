from typing import List, Tuple

folds: List[Tuple[str, int]] = []
dots: List[Tuple[int, int]] = []
paper: List[List[str]] = []
max_height: int = 0
max_width: int = 0

file = open('input13.txt')
line = file.readline()

count: int = 0
while line:
    if line == "\n":
        count += 1
        line = file.readline().strip()
    else:
        line = line.strip()
    if count == 0:
        coords_str: List[str] = line.split(',')
        dots.append((int(coords_str[0]), int(coords_str[1])))
        max_width = max(int(coords_str[0]), max_width)
        max_height = max(int(coords_str[1]), max_height)
    elif count == 1:
        l: List[str] = line.split(" ")
        fold_part: str = l[-1]
        fold_part_split: List[str] = fold_part.split('=')
        folds.append((fold_part_split[0], int(fold_part_split[1])))
    line = file.readline()

file.close()

# build starting paper
for row in range(max_height + 1):
    paper_row: List[str] = []
    for col in range(max_width + 1):
        if (col, row) in dots:
            paper_row.append('#')
        else:
            paper_row.append('.')
    paper.append(paper_row.copy())


def get_new_dots(fold: Tuple[str, int]) -> List[Tuple[int, int]]:
    new_dots: List[Tuple[int, int]] = []
    if fold[0] == 'x':
        for r in range(len(paper)):
            for c in range(fold[1], len(paper[r])):
                if paper[r][c] == '#':
                    new_x: int = c - 2 * (c - fold[1])
                    new_dot: Tuple[int, int] = (new_x, r)
                    new_dots.append(new_dot)
    else:
        for r in range(fold[1], len(paper)):
            for c in range(len(paper[r])):
                if paper[r][c] == '#':
                    new_y: int = r - 2 * (r - fold[1])
                    new_dot: Tuple[int, int] = (c, new_y)
                    new_dots.append(new_dot)
    return new_dots


def reconstruct_paper(fold: Tuple[str, int], fold_dots: List[Tuple[int, int]]) -> None:
    if fold[0] == 'x':
        for r in range(len(paper)):
            for c in range(fold[1]):
                if (c, r) in fold_dots:
                    paper[r][c] = '#'
        for i in range(len(paper)):
            for j in range(len(paper[i]) - 1, fold[1] - 1, -1):
                del paper[i][j]
    else:
        for r in range(fold[1]):
            for c in range(len(paper[r])):
                if (c, r) in fold_dots:
                    paper[r][c] = '#'
        for i in range(len(paper) - 1, fold[1] - 1, -1):
            del paper[i]


for fold in folds:
    d = get_new_dots(fold)
    reconstruct_paper(fold, d)

for row in range(len(paper)):
    print("".join(paper[row]))
