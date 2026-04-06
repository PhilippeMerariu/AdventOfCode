import itertools

file = open('input9_test.txt')
line = file.readline()

result = 0

grid = []
red_tiles = []

while line:
    line = line.strip('\n')
    red_tiles.append(tuple(int(t) for t in line.split(',')))
    line = file.readline()
file.close()

max_rows: int = max([r for _, r in red_tiles]) + 1
max_cols: int = max([c for c, _ in red_tiles]) + 1

# draw grid with red tiles
for r in range(max_rows):
    temp_row = []
    for c in range(max_cols):
        rowcol = (c, r)
        if rowcol in red_tiles:
            temp_row.append('#')
        else:
            temp_row.append('.')
    grid.append(temp_row.copy())

# draw outer loop green tiles
for i in range(len(red_tiles)):
    rt1 = red_tiles[i]
    rt2 = red_tiles[0] if i + 1 >= len(red_tiles) else red_tiles[i + 1]
    if (rt1[0] - rt2[0] == 0):  # same col
        for x in range(min([rt1[1], rt2[1]]) + 1, max([rt1[1], rt2[1]])):
            grid[x][rt1[0]] = 'X'
    else:  # same row
        for x in range(min([rt1[0], rt2[0]]) + 1, max([rt1[0], rt2[0]])):
            grid[rt1[1]][x] = 'X'


# draw inner green tiles
def is_inside_loop(row: int, col: int) -> bool:
    if grid[row][col] in ['#', 'X']:
        return False
    cross_border = 0
    for x in range(row + 1, len(grid)):
        if grid[x][col] in ['#', 'X']:
            cross_border += 1
    return cross_border % 2 == 1 

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if is_inside_loop(r, c):
            grid[r][c] = '+'

for g in grid:
    print(''.join(g))

corner_pairs = itertools.combinations(red_tiles, 2)

for cp in corner_pairs:
    r_size = abs(cp[0][0] - cp[1][0]) + 1
    c_size = abs(cp[0][1] - cp[1][1]) + 1
    volume = r_size * c_size
    if volume > result:
        result = volume

print(f"ANSWER = {result}")
