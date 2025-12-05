file = open('input1.txt')
line = file.readline()

result = 0

rotations = []
arrow = 50

while line:
    line = line.strip('\n')
    rotations.append(line)
    line = file.readline()
file.close()

for r in rotations:
    direction = r[0]
    distance = int(r[1:])
    for _ in range(distance):
        if direction == 'L':
            if arrow == 0:
                arrow = 99
            else:
                arrow -= 1
        elif direction == 'R':
            if arrow == 99:
                arrow = 0
            else:
                arrow += 1
        if arrow == 0:
            result += 1

print(f"ANSWER = {result}")
