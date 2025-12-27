file = open('input4.txt')
line = file.readline()

result = 0

grid = []

while line:
    line = line.strip('\n')
    grid.append(list(line))
    line = file.readline()
file.close()

roll_limit = 4

def count_adjacent_rolls(r: int, c: int) -> int:
    top = r-1
    mid = r
    bot = r+1
    left = c-1
    center = c
    right = c+1
    nb_rolls = 0
    for i in [top, mid, bot]:
        if i < 0 or i > len(grid) - 1:
            continue
        for j in [left, center, right]:
            if j < 0 or j > len(grid[i]) - 1:
                continue
            if (i, j) == (r, c):
                continue
            if grid[i][j] == '@':
                nb_rolls += 1
    return nb_rolls

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '.':
            continue
        adjacent_rolls = count_adjacent_rolls(row, col)
        if adjacent_rolls < roll_limit:
            result += 1


print(f"ANSWER = {result}")
