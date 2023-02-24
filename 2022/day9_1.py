from typing import List

start: complex = complex(0, 0)  # real = col, imaginary = row
head: complex = start
tail: complex = start

visited_positions: List[complex] = [start]

file = open('input9.txt')
line = file.readline().strip()


def is_tail_near() -> bool:
    if abs(head.real - tail.real) <= 1 and abs(head.imag - tail.imag) <= 1:
        return True
    return False
    # if head == tail:  # same position
    #     return True
    # elif head.real == tail.real:
    #     if tail.imag in [head.imag + 1, head.imag - 1]:  # one step above or below
    #         return True
    # elif head.imag == tail.imag:
    #     if tail.real in [head.real + 1, head.real - 1]:  # one step right or left
    #         return True
    # else:


def move_left(n: int) -> None:
    global head
    global tail
    head += complex(-1, 0)


def move_right(n: int) -> None:
    global head
    global tail
    head += complex(1, 0)


def move_up(n: int) -> None:
    global head
    global tail
    head += complex(1, 0)


def move_down(n: int) -> None:
    global head
    global tail
    head += complex(-1, 0)


while line:
    command: List[str] = line.split(" ")
    direction: str = command[0]
    iterations: int = int(command[1])
    for _ in range(iterations):
        if direction == "L":
            move_left(iterations)
        elif direction == "R":
            move_right(iterations)
        elif direction == "U":
            move_up(iterations)
        else:
            move_down(iterations)
        if not is_tail_near():
            pass
    line = file.readline().strip()
file.close()

print("ANSWER = {0}".format())
