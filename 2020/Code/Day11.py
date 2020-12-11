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
            if r == 0 and c == 0:  # first row, first column
                midright = seatMap[r][c+1]
                botmid = seatMap[r+1][c]
                botright = seatMap[r+1][c+1]
            elif r == 0 and c == len(seatMap[r])-1:  # first row, last column
                midleft = seatMap[r][c-1]
                botleft = seatMap[r+1][c-1]
                botmid = seatMap[r+1][c]
            elif r == len(seatMap)-1 and c == 0:  # last row, first column
                topmid = seatMap[r-1][c]
                topright = seatMap[r-1][c+1]
                midright = seatMap[r][c+1]
            elif r == len(seatMap)-1 and c == len(seatMap[r])-1:  # last row, last column
                topleft = seatMap[r-1][c-1]
                topmid = seatMap[r-1][c]
                midleft = seatMap[r][c-1]
            elif r == 0:  # first row
                midleft = seatMap[r][c-1]
                midright = seatMap[r][c+1]
                botleft = seatMap[r+1][c-1]
                botmid = seatMap[r+1][c]
                botright = seatMap[r+1][c+1]
            elif r == len(seatMap)-1:  # last row
                topleft = seatMap[r-1][c-1]
                topmid = seatMap[r-1][c]
                topright = seatMap[r-1][c+1]
                midleft = seatMap[r][c-1]
                midright = seatMap[r][c+1]
            elif c == 0:   # first column
                topmid = seatMap[r-1][c]
                topright = seatMap[r-1][c+1]
                midright = seatMap[r][c+1]
                botmid = seatMap[r+1][c]
                botright = seatMap[r+1][c+1]
            elif c == len(seatMap[r])-1:  # last column
                topleft = seatMap[r-1][c-1]
                topmid = seatMap[r-1][c]
                midleft = seatMap[r][c-1]
                botleft = seatMap[r+1][c-1]
                botmid = seatMap[r+1][c]
            else:  # anywhere else in the middle
                topleft = seatMap[r-1][c-1]
                topmid = seatMap[r-1][c]
                topright = seatMap[r-1][c+1]
                midleft = seatMap[r][c-1]
                midright = seatMap[r][c+1]
                botleft = seatMap[r+1][c-1]
                botmid = seatMap[r+1][c]
                botright = seatMap[r+1][c+1]

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
            elif current == '#' and adjacent.count('#') >= 4:
                toChange.append([r,c])


    changeMade = makeChanges()


print('Result: ' + countSeats())
