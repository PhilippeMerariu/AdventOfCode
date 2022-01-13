from typing import List, Tuple

steps: int = 0

file = open('input11.txt')
line = file.readline().strip()

octopus_grid: List[List[int]] = []
energy_bursts: List[Tuple[int, int]] = []
flashing_lights: int = 0

count: int = 0
while line:
    octopus_grid.append([])
    for nb in line:
        octopus_grid[count].append(int(nb))
    count += 1
    line = file.readline().strip()
file.close()


def increase_energy(row: int, col: int, adjacent: bool = False) -> None:
    global flashing_lights
    # skip if row or col is beyond grid bounds
    if row <= -1 or row >= len(octopus_grid) or col <= -1 or col >= len(octopus_grid):
        return
    # skip adding energy to octopus that already flashed
    if adjacent and octopus_grid[row][col] == 0:
        return
    if octopus_grid[row][col] < 9:
        octopus_grid[row][col] += 1
    else:
        octopus_grid[row][col] = 0
        flashing_lights += 1
        energy_bursts.append((row, col))


def increase_adjacent_energy(center: Tuple[int, int]) -> None:
    r: int = center[0]
    c: int = center[1]
    # top left
    try:
        increase_energy(r - 1, c - 1, True)
    except IndexError:
        pass  # nothing to do
    # top center
    try:
        increase_energy(r - 1, c, True)
    except IndexError:
        pass  # nothing to do
    # top right
    try:
        increase_energy(r - 1, c + 1, True)
    except IndexError:
        pass  # nothing to do
    # center left
    try:
        increase_energy(r, c - 1, True)
    except IndexError:
        pass  # nothing to do
    # center right
    try:
        increase_energy(r, c + 1, True)
    except IndexError:
        pass  # nothing to do
    # bottom left
    try:
        increase_energy(r + 1, c - 1, True)
    except IndexError:
        pass  # nothing to do
    # bottom center
    try:
        increase_energy(r + 1, c, True)
    except IndexError:
        pass  # nothing to do
    # bottom right
    try:
        increase_energy(r + 1, c + 1, True)
    except IndexError:
        pass  # nothing to do


def all_octopuses() -> bool:
    all_burst: bool = True
    for r in range(len(octopus_grid)):
        for c in range(len(octopus_grid[r])):
            if octopus_grid[r][c] != 0:
                return False
    return True


while not all_octopuses():
    energy_bursts.clear()
    for row in range(len(octopus_grid)):
        for col in range(len(octopus_grid[row])):
            if octopus_grid[row][col] < 9:
                octopus_grid[row][col] += 1
            else:
                flashing_lights += 1
                octopus_grid[row][col] = 0
                energy_bursts.append((row, col))

    for burst in energy_bursts:
        increase_adjacent_energy(burst)

    steps += 1

print("ANSWER = {0}".format(steps))
