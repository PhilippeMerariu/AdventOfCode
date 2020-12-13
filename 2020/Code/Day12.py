northSouth = 0
eastWest = 0

directionVal = 0
direction = {0: 'east', 1: 'south', 2: 'west', 3: 'north'}

file = open('input12.txt')
line = file.readline().replace('\n', '')

while line:
    char = line[0]
    amount = int(line[1:])

    if char == 'N':
        northSouth += amount
    elif char == 'S':
        northSouth -= amount
    elif char == 'E':
        eastWest += amount
    elif char == 'W':
        eastWest -= amount
    elif char == 'F':
        if direction.get(directionVal) == 'north':
            northSouth += amount
        elif direction.get(directionVal) == 'south':
            northSouth -= amount
        elif direction.get(directionVal) == 'east':
            eastWest += amount
        else: # char == 'W'
            eastWest -= amount
    elif char == 'L':
        amount /= 90
        directionVal -= amount
        if directionVal < 0:
            directionVal += 4
    else: # char == 'R'
        amount /= 90
        directionVal += amount
        if directionVal > 3:
            directionVal -= 4

    line = file.readline().replace('\n', '')
file.close()

total = abs(northSouth) + abs(eastWest)


print('Result: ' + str(total))
