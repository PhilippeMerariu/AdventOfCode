from math import floor


def checkAround():
    around = []
    for z in grid:
        plane = grid.get(z)
        topPlane = []
        bottomPlane = []
        try:
            topPlane = grid.get(z-1)
        except:
            print("not plane above")
        try:
            bottomPlane = grid.get(z+1)
        except:
            print("no plane below")
        for r in range(len(plane)):
            for c in range(len(plane[r])):
                currentCube = plane[r][c]
                around.clear()
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if topPlane:
                            if 0 <= r+i < len(topPlane) and 0 <= c+j < len(topPlane):
                                around.append(topPlane[r+i][c+j])
                            else:
                                around.append('.')
                        if bottomPlane:
                            if 0 <= r+i < len(bottomPlane) and 0 <= c+j < len(bottomPlane):
                                around.append(bottomPlane[r+i][c+j])
                            else:
                                around.append('.')
                        if 0 <= r+i < len(plane) and 0 <= c+j < len(plane):
                            around.append(plane[r+i][c+j])
                        else:
                            around.append('.')
                nbCubes = around.count('#')
                if currentCube == '#':
                    nbCubes -= 1
                checkRule(currentCube, nbCubes, [r, c, z])

def checkRule(current, nbCubes, coord):
    if current == "#" and nbCubes not in [2, 3]:
        toChange.append(coord)
    elif current == '.' and nbCubes == 3:
        toChange.append(coord)

def applyChanges():
    for change in toChange:
        row = change[0]
        col = change[1]
        level = change[2]
        if grid.get(level)[row][col] == '.':
            grid.get(level)[row][col] = '#'
        else:
            grid.get(level)[row][col] = '.'

    toChange.clear()

def growCube():
    newRow = []
    for z in grid:
        newRow.clear()
        plane = grid.get(z)
        blankRow = ['.']*(len(plane)+2)
        newRow.append(blankRow.copy())
        for r in range(len(plane)):
            prevRow = plane[r].copy()
            prevRow.insert(0, '.')
            prevRow.append('.')
            newRow.append(prevRow.copy())
        newRow.append(blankRow.copy())
        grid.update({z: newRow.copy()})
    dimension = floor(len(newRow) / 2)
    newPlane = []
    newRow = ['.'] * len(newRow)
    for i in range(len(newRow)):
        newPlane.append(newRow.copy())
    grid.update({-dimension: newPlane})
    grid.update({dimension: newPlane})


def countCubes():
    res = 0
    for level in grid:
        level = grid.get(level)
        for l in level:
            res += l.count('#')
    print(res)


grid = {}
cubeRow = []
cubePlane = []

file = open('input17_test.txt')
line = file.readline().replace('\n', '')

cubeRow = ['.']*len(line)
dimension = floor(len(line)/2)
for i in range(-dimension, dimension+1):
    cubePlane.clear()
    for j in range(len(line)):
        cubePlane.append(cubeRow.copy())
    grid.update({i: cubePlane.copy()})

cubePlane.clear()

z = 0
cycle = 0

toChange = []

while line:
    line = line.replace('\n', '')
    cubeRow.clear()
    for cube in line:
        cubeRow.append(cube)
    cubePlane.append(cubeRow.copy())
    line = file.readline()
file.close()

grid.update({z: cubePlane.copy()})

while cycle <= 6:
    if cycle > 0:
        growCube()
        grid = dict(sorted(grid.items()))
    checkAround()
    applyChanges()
    cycle += 1
    countCubes()



# print("Result: " + str(res))
