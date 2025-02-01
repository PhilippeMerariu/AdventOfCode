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

def obstacle_in_sight(r, c, direction):
    match direction:
        case "^":
            for i in range(0, r):
                if lab[i][c] == "#":
                    return True
            return False
        case ">":
            for i in range(c, len(lab)):
                if lab[r][i] == "#":
                    return True
            return False
        case "<":
            for i in range(0, c):
                if lab[r][i] == "#":
                    return True
            return False
        case "v":
            for i in range(r, len(lab)):
                if lab[i][c] == "#":
                    return True
            return False

def is_loop(r, c):
    pass

loops = 0
# for row in range(len(lab)):
#     for col in range(len(lab)):
#         if lab[row][col] in ["^", "#"]:
#             continue
#         if is_loop(row, col):
#             loops += 1

while True:
    guard_row, guard_col = guard
    guard_dir = lab[guard_row][guard_col]
    print(guard)
    match guard_dir:
        case "^":
            if is_end(guard_row - 1, guard_col):
                break
            if can_move(guard_row - 1, guard_col):
                if obstacle_in_sight(guard_row, guard_col, ">"):
                    print(guard)
                    break
                lab[guard_row - 1][guard_col] = "^"
                guard = (guard_row - 1, guard_col)
            else:
                lab[guard_row][guard_col] = ">"
        case ">":
            if is_end(guard_row, guard_col + 1):
                break
            if can_move(guard_row, guard_col + 1):
                lab[guard_row][guard_col + 1] = ">"
                guard = (guard_row, guard_col + 1)
            else:
                lab[guard_row][guard_col] = "v"
        case "<":
            if is_end(guard_row, guard_col - 1):
                break
            if can_move(guard_row, guard_col - 1):
                lab[guard_row][guard_col - 1] = "<"
                guard = (guard_row, guard_col - 1)
            else:
                lab[guard_row][guard_col] = "^"
        case "v":
            if is_end(guard_row + 1, guard_col):
                break
            if can_move(guard_row + 1, guard_col):
                lab[guard_row + 1][guard_col] = "v"
                guard = (guard_row + 1, guard_col)
            else:
                lab[guard_row][guard_col] = "<"

print(f"ANSWER = {loops}")
