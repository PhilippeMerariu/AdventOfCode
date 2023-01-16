from typing import List, Dict

file = open('input3.txt')
line = file.readline()

rucksack: str = ""
compart_1: str = ""
compart_2: str = ""

common: List[str] = []

while line:
    rucksack = line.strip()
    compart_1 = rucksack[:int(len(rucksack)/2)]
    compart_2 = rucksack[int(len(rucksack)/2):]
    for c in compart_1:
        if c in compart_2:
            common.append(c)
            break
    line = file.readline()
file.close()

priority: Dict[str, int] = {}
value: int = 1

for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    priority.update({letter: value})
    value += 1

answer: int = 0
for letter in common:
    answer += priority.get(letter)

print("ANSWER = {0}".format(answer))
