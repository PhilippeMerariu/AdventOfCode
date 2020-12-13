def flipDirection():
    waypoint[0] = abs(waypoint[0])
    waypoint[1] = abs(waypoint[1])
    if direction.get(directionVal[0]) in ['south', 'west']:
        waypoint[0] = -waypoint[0]
    if direction.get(directionVal[1]) in ['south', 'west']:
        waypoint[1] = -waypoint[1]

def correctDirection():
    if direction.get(directionVal[0]) in ['north', 'east'] and waypoint[0] < 0:
        directionVal[0] += 2
        if directionVal[0] > 3:
            directionVal[0] -= 4
    if direction.get(directionVal[0]) in ['south', 'west'] and waypoint[0] > 0:
        directionVal[0] += 2
        if directionVal[0] > 3:
            directionVal[0] -= 4
    if direction.get(directionVal[1]) in ['north', 'east'] and waypoint[1] < 0:
        directionVal[1] += 2
        if directionVal[1] > 3:
            directionVal[1] -= 4
    if direction.get(directionVal[1]) in ['south', 'west'] and waypoint[1] > 0:
        directionVal[1] += 2
        if directionVal[1] > 3:
            directionVal[1] -= 4



northSouth = 0
eastWest = 0

waypoint = [1, 10]
directionVal = [3, 0]
direction = {0: 'east', 1: 'south', 2: 'west', 3: 'north'}

file = open('input12.txt')
line = file.readline().replace('\n', '')

while line:
    char = line[0]
    amount = int(line[1:])

    if char == 'N':
        if direction.get(directionVal[0]) in ['north', 'south']:
            waypoint[0] += amount
        else:
            waypoint[1] += amount
        print("move waypoint " + str(amount) + " north")
    elif char == 'S':
        if direction.get(directionVal[0]) in ['north', 'south']:
            waypoint[0] -= amount
        else:
            waypoint[1] -= amount
        print("move waypoint " + str(amount) + " south")
    elif char == 'E':
        if direction.get(directionVal[0]) in ['east', 'west']:
            waypoint[0] += amount
        else:
            waypoint[1] += amount
        print("move waypoint " + str(amount) + " east")
    elif char == 'W':
        if direction.get(directionVal[0]) in ['east', 'west']:
            waypoint[0] -= amount
        else:
            waypoint[1] -= amount
        print("move waypoint " + str(amount) + " west")
    elif char == 'F':
        if direction.get(directionVal[0]) in ['north', 'south']:
            northSouth += waypoint[0]*amount
            eastWest += waypoint[1]*amount
            print("move ship " + str(waypoint[0]*amount) + " north and " + str(waypoint[1]*amount) + " east")
        else:
            northSouth += waypoint[1] * amount
            eastWest += waypoint[0] * amount
            print("move ship " + str(waypoint[1] * amount) + " north and " + str(waypoint[0] * amount) + " east")
    elif char == 'L':
        amount /= 90
        directionVal[0] -= amount
        if directionVal[0] < 0:
            directionVal[0] += 4
        directionVal[1] -= amount
        if directionVal[1] < 0:
            directionVal[1] += 4
        flipDirection()
    else: # char == 'R'
        amount /= 90
        directionVal[0] += amount
        if directionVal[0] > 3:
            directionVal[0] -= 4
        directionVal[1] += amount
        if directionVal[1] > 3:
            directionVal[1] -= 4
        flipDirection()

    correctDirection()

    line = file.readline().replace('\n', '')
file.close()

total = abs(northSouth) + abs(eastWest)


print('Result: ' + str(total))
