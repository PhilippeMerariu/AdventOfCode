from typing import List

ROUND_POINTS: int = 3
SQUARE_POINTS: int = 57
SQUIGGLY_POINTS: int = 1197
ANGLED_POINTS: int = 25137

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
illegal_chars: List[str] = []

while line:
    lines.append(line)
    line = file.readline().strip()
file.close()

for l in lines:
    for i in range(len(l)):
        if l[i] in OPEN_BRACKETS:
            bracket_stack.append(l[i])
        elif OPEN_BRACKETS.index(bracket_stack.pop()) != CLOSE_BRACKETS.index(l[i]):
            illegal_chars.append(l[i])

answer: int = 0
for char in illegal_chars:
    answer += BRACKET_POINTS[CLOSE_BRACKETS.index(char)]

print("ANSWER = {0}".format(answer))
