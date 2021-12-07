from typing import List

file = open('input5.txt')
line = file.readline().strip()

lines: List[List[List[int]]] = []
coords: List[List[int]] = []
grid_size: int = 0

while line:
    temp = line.strip().split(" ->")
    for t in temp:
        coords.append([int(x) for x in t.split(",")])
    if coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]:
        lines.append(coords.copy())
        # get grid size
        for c in coords:
            for val in c:
                if val > grid_size:
                    grid_size = val + 1
    coords.clear()
    line = file.readline()
file.close()

# construct empty grid
grid: List[List[str]] = []
for i in range(grid_size):
    grid_row: List[str] = []
    for j in range(grid_size):
        grid_row.append('.')
    grid.append(grid_row.copy())


def fill_line(x: int, y: int):
    if grid[x][y] == '.':
        grid[x][y] = '1'
    else:
        grid[x][y] = str(int(grid[x][y]) + 1)


def draw_horizontal(col: int, start: int, end: int):
    for i in range(min(start, end), max(start, end) + 1):
        fill_line(col, i)


def draw_vertical(row: int, start: int, end: int):
    for i in range(min(start, end), max(start, end) + 1):
        fill_line(i, row)


def draw_line(start: List[int], end: List[int]):
    if start[0] == end[0]:
        draw_vertical(start[0], start[1], end[1])
    else:
        draw_horizontal(start[1], start[0], end[0])


for l in lines:
    draw_line(l[0], l[1])

answer: int = 0
for g in grid:
    for val in g:
        try:
            if int(val) >= 2:
                answer += 1
        except:
            pass


print("ANSWER = {0}".format(answer))
