file = open('input6.txt')
line = file.readline()

lab = []
guard = (-1, -1)

labrow = 0
while line:
    line = line.strip('\n')
    labline = []
    for labcol in range(len(line)):
        if line[labcol] == "^":
            guard = (labrow, labcol)
        labline.append(line[labcol])
    lab.append(labline.copy())
    labrow += 1
    line = file.readline()
file.close()

def can_move(r, c):
    return lab[r][c] != "#"

def is_end(r, c):
    if 0 <= r <= (len(lab)-1) and 0 <= c <= (len(lab)-1):
        return False
    return True

while True:
    guard_row, guard_col = guard
    guard_dir = lab[guard_row][guard_col]
    match guard_dir:
        case "^":
            if is_end(guard_row - 1, guard_col):
                lab[guard_row][guard_col] = "X"
                break
            if can_move(guard_row - 1, guard_col):
                lab[guard_row][guard_col] = "X"
                lab[guard_row - 1][guard_col] = "^"
                guard = (guard_row - 1, guard_col)
            else:
                lab[guard_row][guard_col] = ">"
        case ">":
            if is_end(guard_row, guard_col + 1):
                lab[guard_row][guard_col] = "X"
                break
            if can_move(guard_row, guard_col + 1):
                lab[guard_row][guard_col] = "X"
                lab[guard_row][guard_col + 1] = ">"
                guard = (guard_row, guard_col + 1)
            else:
                lab[guard_row][guard_col] = "v"
        case "<":
            if is_end(guard_row, guard_col - 1):
                lab[guard_row][guard_col] = "X"
                break
            if can_move(guard_row, guard_col - 1):
                lab[guard_row][guard_col] = "X"
                lab[guard_row][guard_col - 1] = "<"
                guard = (guard_row, guard_col - 1)
            else:
                lab[guard_row][guard_col] = "^"
        case "v":
            if is_end(guard_row + 1, guard_col):
                lab[guard_row][guard_col] = "X"
                break
            if can_move(guard_row + 1, guard_col):
                lab[guard_row][guard_col] = "X"
                lab[guard_row + 1][guard_col] = "v"
                guard = (guard_row + 1, guard_col)
            else:
                lab[guard_row][guard_col] = "<"

visited_spots = 0
for row in lab:
    for space in row:
        if space == "X":
            visited_spots += 1

print(f"ANSWER = {visited_spots}")
