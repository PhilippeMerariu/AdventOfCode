from typing import List

import numpy

ROUND_POINTS: int = 1
SQUARE_POINTS: int = 2
SQUIGGLY_POINTS: int = 3
ANGLED_POINTS: int = 4

BRACKET_POINTS: List[int] = [ROUND_POINTS, SQUARE_POINTS, SQUIGGLY_POINTS, ANGLED_POINTS]

ROUND_BRACKET_OPEN: str = '('
ROUND_BRACKET_CLOSE: str = ')'

SQUARE_BRACKET_OPEN: str = '['
SQUARE_BRACKET_CLOSE: str = ']'

SQUIGGLY_BRACKET_OPEN: str = '{'
SQUIGGLY_BRACKET_CLOSE: str = '}'

ANGLED_BRACKET_OPEN: str = '<'
ANGLED_BRACKET_CLOSE: str = '>'

OPEN_BRACKETS: List[str] = [ROUND_BRACKET_OPEN, SQUARE_BRACKET_OPEN, SQUIGGLY_BRACKET_OPEN, ANGLED_BRACKET_OPEN]
CLOSE_BRACKETS: List[str] = [ROUND_BRACKET_CLOSE, SQUARE_BRACKET_CLOSE, SQUIGGLY_BRACKET_CLOSE, ANGLED_BRACKET_CLOSE]

file = open('input10.txt')
line = file.readline().strip()

lines: List[str] = []
bracket_stack: List[str] = []
bracket_stacks: List[List[str]] = []
illegal_lines: List[int] = []

while line:
    lines.append(line)
    line = file.readline().strip()
file.close()

for l in lines:
    for i in range(len(l)):
        if l[i] in OPEN_BRACKETS:
            bracket_stack.append(l[i])
        elif OPEN_BRACKETS.index(bracket_stack.pop()) != CLOSE_BRACKETS.index(l[i]):
            illegal_lines.append(lines.index(l))
    bracket_stacks.append(bracket_stack.copy())
    bracket_stack.clear()

# clean up lines
illegal_lines = sorted(illegal_lines, reverse=True)
for illegal in illegal_lines:
    lines.pop(illegal)
    bracket_stacks.pop(illegal)

answer: List[int] = []
for bracket_list in bracket_stacks:
    answer.append(0)
    for i in range(len(bracket_list)):
        answer[-1] = answer[-1] * 5 + BRACKET_POINTS[OPEN_BRACKETS.index(bracket_list.pop())]


print("ANSWER = {0}".format(int(numpy.median(answer))))
