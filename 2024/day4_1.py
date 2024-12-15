file = open('input4.txt')
line = file.readline()

grid = []
all_x = []
found_xmases = 0

def find_xmas(row, col, dir_r, dir_c):
    global found_xmases

    word = grid[row][col]
    r2 = row
    c2 = col
    for _ in range(3):
        r2 += dir_r
        c2 += dir_c
        if -1 < r2 < len(grid) and -1 < c2 < len(grid):
            word += grid[r2][c2]
        else:
            return
    if word == "XMAS":
        found_xmases += 1

while line:
    gridline = [x for x in line.strip('\n')]
    grid.append(gridline.copy())
    line = file.readline()
file.close()

for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == 'X':
            all_x.append((row, col))

for r, c in all_x:
    find_xmas(r, c, dir_r=-1, dir_c=0)  # NORTH
    find_xmas(r, c, dir_r=1, dir_c=0)  # SOUTH
    find_xmas(r, c, dir_r=0, dir_c=-1)  # WEST
    find_xmas(r, c, dir_r=0, dir_c=1)  # EAST
    find_xmas(r, c, dir_r=-1, dir_c=-1)  # NORTH WEST
    find_xmas(r, c, dir_r=-1, dir_c=1)  # NORTH EAST
    find_xmas(r, c, dir_r=1, dir_c=-1)  # SOUTH WEST
    find_xmas(r, c, dir_r=1, dir_c=1)  # SOUTH EAST

# print(all_x, len(all_x))
print(f"ANSWER = {found_xmases}")
