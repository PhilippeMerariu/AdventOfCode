from typing import List

STEPS: int = 100

file = open('input11_test.txt')
line = file.readline().strip()

octopus_grid: List[List[int]] = []
flashing_lights: int = 0

count: int = 0
while line:
    octopus_grid.append([])
    for nb in line:
        octopus_grid[count].append(int(nb))
    count += 1
    line = file.readline().strip()
file.close()

answer: int = 0

print("ANSWER = {0}".format(answer))
