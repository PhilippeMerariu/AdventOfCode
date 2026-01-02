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

for row in grid[1:]:
    new_beams = beams.copy()
    for beam in beams:
        if row[beam] == '.':
            row[beam] = '|'
        elif row[beam] == '^':
            result += 1
            new_beams.remove(beam)
            new_beams.append(beam - 1)
            new_beams.append(beam + 1)
    beams = list(set(new_beams)).copy()

print(f"ANSWER = {result}")
