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

boards.update({count: board.copy()})


def search_boards(nb: int):
    for i in boards:
        brd: List[List[int]] = boards.get(i).copy()
        for b in brd:
            for i in range(len(b)):
                if b[i] == nb:
                    b[i] = -1
        boards.update({i: brd})


def check_rows() -> List[int]:
    completed_rows: List[int] = []
    for i in boards:
        brd: List[List[int]] = boards.get(i)
        for b in brd:
            if all(x == -1 for x in b):
                completed_rows.append(i)
    return completed_rows


def check_cols() -> List[int]:
    completed_cols: List[int] = []
    for i in boards:
        brd: List[List[int]] = boards.get(i)
        col: bool = True
        for j in range(len(brd)):
            for b in brd:
                if b[j] != -1:
                    col = False
            if col:
                completed_cols.append(i)
    return completed_cols


def calculate_result(index: int, nb: int) -> int:
    result: int = 0
    brd: List[List[int]] = boards.get(index)
    for b in brd:
        for val in b:
            if val != -1:
                result += val
    return result * nb


answer: int = 0
copy_boards = boards.copy()

# start bingo game
for nb in numbers:
    search_boards(nb)
    rows = check_rows()
    cols = check_cols()
    for r in rows:
        try:
            copy_boards.pop(r)
        except KeyError:
            pass
    for c in cols:
        try:
            copy_boards.pop(c)
        except KeyError:
            pass
    if len(copy_boards) == 1:
        answer = calculate_result(list(copy_boards.keys())[0], nb)
        break

print("ANSWER = {0}".format(answer))
