from typing import List, Dict

UNIQUE_VALUES: List[int] = [2, 3, 4, 7]

file = open('input8.txt')
line = file.readline().strip()

inputs: Dict[int, List[str]] = {}
outputs: Dict[int, List[str]] = {}

count: int = 0

while line:
    in_out: List[str] = line.split(" | ")
    inputs.update({count: in_out[0].split(" ")})
    outputs.update({count: in_out[1].split(" ")})
    count += 1
    line = file.readline().strip()
file.close()

answer: int = 0
for _, out in outputs.items():
    for val in out:
        if len(val) in UNIQUE_VALUES:
            answer += 1

print("ANSWER = {0}".format(answer))
