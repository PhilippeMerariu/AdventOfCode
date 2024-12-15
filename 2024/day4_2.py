file = open('input4.txt')
line = file.readline()

grid = []
all_a = []
found_xmases = 0

def find_xmas(row, col):
    first_r1 = row - 1
    first_c1 = col - 1
    first_r2 = row + 1
    first_c2 = col + 1

    second_r1 = row - 1
    second_c1 = col + 1
    second_r2 = row + 1
    second_c2 = col - 1

    if -1 < first_r1 < len(grid) and -1 < first_c1 < len(grid) \
            and -1 < first_r2 < len(grid) and -1 < first_c2 < len(grid) \
            and -1 < second_r1 < len(grid) and -1 < second_c1 < len(grid) \
            and -1 < second_r2 < len(grid) and -1 < second_c2 < len(grid):
        first_diag = grid[first_r1][first_c1] + grid[row][col] + grid[first_r2][first_c2]
        second_diag = grid[second_r1][second_c1] + grid[row][col] + grid[second_r2][second_c2]
        if first_diag in ["MAS", "SAM"] and second_diag in ["MAS", "SAM"]:
            return 1
    return 0

while line:
    gridline = [x for x in line.strip('\n')]
    grid.append(gridline.copy())
    line = file.readline()
file.close()

for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == 'A':
            all_a.append((row, col))

for r, c in all_a:
    found_xmases += find_xmas(r, c)

# print(all_x, len(all_x))
print(f"ANSWER = {found_xmases}")
