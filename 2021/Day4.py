from typing import List, Dict


def create_board_line(values: str) -> List[int]:
    values = values.strip().split(" ")
    values = list(filter(len, values))
    return [int(x) for x in values]


file = open('input4.txt')
line = file.readline().strip()

numbers: List[int] = []
boards: Dict[int, List[List[int]]] = {}
board: List[List[int]] = []

temp: List[str] = line.split(",")
for t in temp:
    numbers.append(int(t))

count: int = 0

line = file.readline()
while line:
    if line == "\n":
        if board:
            boards.update({count: board.copy()})
            board.clear()
            count += 1
    else:
        board.append(create_board_line(line))
    line = file.readline()
file.close()


def search_boards(nb: int):
    for i in boards:
        brd: List[List[int]] = boards.get(i).copy()
        for b in brd:
            for i in range(len(b)):
                if b[i] == nb:
                    b[i] = -1
        boards.update({i: brd})


def check_rows() -> int:
    for i in boards:
        brd: List[List[int]] = boards.get(i)
        for b in brd:
            if all(x == -1 for x in b):
                return i
    return -1


def check_cols() -> int:
    for i in boards:
        brd: List[List[int]] = boards.get(i)
        col: bool = True
        for j in range(len(brd)):
            for b in brd:
                if b[j] != -1:
                    col = False
            if col:
                return i
    return -1


def calculate_result(index: int, nb: int) -> int:
    result: int = 0
    brd: List[List[int]] = boards.get(index)
    for b in brd:
        for val in b:
            if val != -1:
                result += val
    return result * nb


answer: int = 0

# start bingo game
for nb in numbers:
    search_boards(nb)
    row = check_rows()
    col = check_cols()
    if row > -1:
        answer = calculate_result(row, nb)
        break
    if col > -1:
        answer = calculate_result(col, nb)
        break

print("ANSWER = {0}".format(answer))
