from typing import List, Tuple

folds: List[Tuple[str, int]] = []
paper: List[List[str]] = []
max_height: int = 0
max_width: int = 0

file = open('input13_test.txt')
line = file.readline().strip()

while line:
    line = file.readline().strip()
file.close()

answer: int = 0
print("ANSWER = {0}".format(answer))
