def makeChanges():
    print(str(len(toChange)) + " changes made")
    if len(toChange) == 0:
        return False
    else:
        for change in toChange:
            row = change[0]
            col = change[1]
            if seatMap[row][col] == 'L':
                seatMap[row][col] = '#'
            else:
                seatMap[row][col] = 'L'
        toChange.clear()
        return True

def countSeats():
    count = 0
    for row in range(len(seatMap)):
        for col in range(len(seatMap[r])):
            if seatMap[row][col] == '#':
                count += 1
    return str(count)

def findTopLeft(row, col):
    row -= 1
    col -= 1
    tl = seatMap[row][col]
    while (tl != 'L' and tl != '#') and (row > 0 and col > 0):
        row -= 1
        col -= 1
        tl = seatMap[row][col]
    return tl

def findTopMid(row, col):
    row -= 1
    tm = seatMap[row][col]
    while (tm != 'L' and tm != '#') and row > 0:
        row -= 1
        tm = seatMap[row][col]
    return tm

def findTopRight(row, col):
    row -= 1
    col += 1
    tr = seatMap[row][col]
    while (tr != 'L' and tr != '#') and (row > 0 and col < len(seatMap[row])-1):
        row -= 1
        col += 1
        tr = seatMap[row][col]
    return tr

def findMidLeft(row, col):
    col -= 1
    ml = seatMap[row][col]
    while (ml != 'L' and ml != '#') and col > 0:
        col -= 1
        ml = seatMap[row][col]
    return ml

def findMidRight(row, col):
    col += 1
    mr = seatMap[row][col]
    while (mr != 'L' and mr != '#') and col < len(seatMap[row])-1:
        col += 1
        mr = seatMap[row][col]
    return mr

def findBotLeft(row, col):
    row += 1
    col -= 1
    bl = seatMap[row][col]
    while (bl != 'L' and bl != '#') and (row < len(seatMap)-1 and col > 0):
        row += 1
        col -= 1
        bl = seatMap[row][col]
    return bl

def findBotMid(row, col):
    row += 1
    rm = seatMap[row][col]
    while (rm != 'L' and rm != '#') and row < len(seatMap)-1:
        row += 1
        rm = seatMap[row][col]
    return rm

def findBotRight(row, col):
    row += 1
    col += 1
    br = seatMap[row][col]
    while (br != 'L' and br != '#') and (row < len(seatMap)-1 and col < len(seatMap[row])-1):
        row += 1
        col += 1
        br = seatMap[row][col]
    return br


seatMap = []
seatRow = []
toChange = []
changeMade = True

file = open('input11.txt')
line = file.readline().replace('\n', '')

while line:
    seatRow.clear()
    for seat in line:
        seatRow.append(seat)
    seatMap.append(seatRow.copy())
    line = file.readline().replace('\n', '')
file.close()

while changeMade:
    for r in range(len(seatMap)):
        for c in range(len(seatMap[r])):
            topleft = ''
            topmid = ''
            topright = ''
            midleft = ''
            midright = ''
            botleft = ''
            botmid = ''
            botright = ''
            adjacent = []
            current = seatMap[r][c]
            if current != '.':
                if r == 0 and c == 0:  # first row, first column
                    midright = findMidRight(r, c)
                    botmid = findBotMid(r, c)
                    botright = findBotRight(r, c)
                elif r == 0 and c == len(seatMap[r])-1:  # first row, last column
                    midleft = findMidLeft(r, c)
                    botleft = findBotLeft(r, c)
                    botmid = findBotMid(r, c)
                elif r == len(seatMap)-1 and c == 0:  # last row, first column
                    topmid = findTopMid(r, c)
                    topright = findTopRight(r, c)
                    midright = findMidRight(r, c)
                elif r == len(seatMap)-1 and c == len(seatMap[r])-1:  # last row, last column
                    topleft = findTopLeft(r, c)
                    topmid = findTopMid(r, c)
                    midleft = findMidLeft(r, c)
                elif r == 0:  # first row
                    midleft = findMidLeft(r, c)
                    midright = findMidRight(r, c)
                    botleft = findBotLeft(r, c)
                    botmid = findBotMid(r, c)
                    botright = findBotRight(r, c)
                elif r == len(seatMap)-1:  # last row
                    topleft = findTopLeft(r, c)
                    topmid = findTopMid(r, c)
                    topright = findTopRight(r, c)
                    midleft = findMidLeft(r, c)
                    midright = findMidRight(r, c)
                elif c == 0:   # first column
                    topmid = findTopMid(r, c)
                    topright = findTopRight(r, c)
                    midright = findMidRight(r, c)
                    botmid = findBotMid(r, c)
                    botright = findBotRight(r, c)
                elif c == len(seatMap[r])-1:  # last column
                    topleft = findTopLeft(r, c)
                    topmid = findTopMid(r, c)
                    midleft = findMidLeft(r, c)
                    botleft = findBotLeft(r, c)
                    botmid = findBotMid(r, c)
                else:  # anywhere else in the middle
                    topleft = findTopLeft(r, c)
                    topmid = findTopMid(r, c)
                    topright = findTopRight(r, c)
                    midleft = findMidLeft(r, c)
                    midright = findMidRight(r, c)
                    botleft = findBotLeft(r, c)
                    botmid = findBotMid(r, c)
                    botright = findBotRight(r, c)

                adjacent.append(topleft)
                adjacent.append(topmid)
                adjacent.append(topright)
                adjacent.append(midleft)
                adjacent.append(midright)
                adjacent.append(botleft)
                adjacent.append(botmid)
                adjacent.append(botright)

                if current == 'L' and adjacent.count('#') == 0:
                    toChange.append([r,c])
                elif current == '#' and adjacent.count('#') >= 5:
                    toChange.append([r,c])


    changeMade = makeChanges()


print('Result: ' + countSeats())
