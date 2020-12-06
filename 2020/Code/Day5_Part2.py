def findRow(rowCode, rows):
    seatRow = rows
    for char in rowCode:
        if char == 'F':
            seatRow = seatRow[:len(seatRow)//2]
        else:
            seatRow = seatRow[len(seatRow)//2:]
    return seatRow[0]

def findCol(colCode, cols):
    seatCol = cols
    for char in colCode:
        if char == 'L':
            seatCol = seatCol[:len(seatCol)//2]
        else:
            seatCol = seatCol[len(seatCol)//2:]
    return seatCol[0]

def calcID(row, col):
    return row * 8 + col

rows = [0]*128
cols = [0]*8
seatID = []
for i in range(0, 128):
    rows[i] = i

for j in range(0, 8):
    cols[j] = j

file = open('input5.txt')
line = file.readline().replace('\n', '')

while line:
    rowCode = line[:-3]
    colCode = line[-3:]
    r = findRow(rowCode, rows)
    c = findCol(colCode, cols)
    seatID.append(calcID(r, c))
    line = file.readline().replace('\n', '')
file.close()

sortedSeats = sorted(seatID)

startingID = sortedSeats[0]
for id in range(startingID, len(sortedSeats)):
    if id not in sortedSeats:
        print("Your seat is ID: " + str(id))

# print("Result: " + str(max(seatID)))
