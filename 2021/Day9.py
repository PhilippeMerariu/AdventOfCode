from typing import List

file = open('input9.txt')
line = file.readline().strip()

cave_map: List[str] = []
lowpoints: List[int] = []

while line:
    cave_map.append(line)
    line = file.readline().strip()
file.close()


def get_adjacent(row: int, col: int, height: int, width: int) -> List[int]:
    adjacent: List[int] = []
    if row > 0:
        adjacent.append(int(cave_map[row - 1][col]))  # top
    if row < height:
        adjacent.append(int(cave_map[row + 1][col]))  # bottom
    if col > 0:
        adjacent.append(int(cave_map[row][col - 1]))  # left
    if col < width:
        adjacent.append(int(cave_map[row][col + 1]))  # right
    return adjacent


for i in range(len(cave_map)):
    for j in range(len(cave_map[i])):
        current: int = int(cave_map[i][j])
        adj: List[int] = get_adjacent(i, j, len(cave_map)-1, len(cave_map[i])-1)
        if all(current < i for i in adj):
            lowpoints.append(current)

for i in range(len(lowpoints)):
    lowpoints[i] += 1
answer: int = sum(lowpoints)


print("ANSWER = {0}".format(answer))
