from typing import List

file = open('input5.txt')
line = file.readline()

stacks: List[List[str]] = [
    ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
    ['D', 'W', 'B'],
    ['T', 'S', 'Q', 'W', 'J', 'C'],
    ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
    ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
    ['B', 'W', 'F', 'T', 'N'],
    ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
    ['H', 'P', 'F', 'R'],
    ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']
]

move_section: bool = False
move: int = -1
stack_from: int = -1
stack_to: int = -1


def move_crates(moves: int, frm: int, to: int) -> None:
    frm = frm - 1
    to = to - 1
    for _ in range(moves):
        stacks[to].append(stacks[frm][-1])
        del stacks[frm][-1]


while line:
    if line == "\n":
        move_section = True
    if not move_section:
        line = file.readline()
        continue
    line = file.readline()
    if line:
        data = line.split(" ")
        move = int(data[1])
        stack_from = int(data[3])
        stack_to = int(data[5])
        move_crates(move, stack_from, stack_to)
file.close()

final_crates: str = ""
for s in stacks:
    final_crates += s[-1]

print("ANSWER = {0}".format(final_crates))
