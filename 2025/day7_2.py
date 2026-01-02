from functools import lru_cache

file = open('input7.txt')
line = file.readline()

result = 0

grid = []

while line:
    line = line.strip('\n')
    grid.append([l for l in line])
    line = file.readline()
file.close()


start = grid[0].index('S')
beams = [start]

def count_paths(grid, start_col):
    rows = len(grid)
    cols = len(grid[0])

    @lru_cache(None)
    def dfs(r, c):
        # Out of bounds → no path
        if c < 0 or c >= cols:
            return 0

        # Reached bottom row → valid path
        if r == rows - 1:
            return 1

        # Cell directly below
        below = grid[r + 1][c]

        # Free → continue straight down
        if below == '.':
            return dfs(r + 1, c)

        # Barrier → split left and right
        paths = 0
        paths += dfs(r + 1, c - 1)
        paths += dfs(r + 1, c + 1)
        return paths

    return dfs(0, start_col)

result = count_paths(grid, start)

print(f"ANSWER = {result}")
