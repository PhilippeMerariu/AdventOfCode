from typing import List, Dict

file = open('input3.txt')
line = file.readline()

rucksack: str = ""
group: List[str] = []

common: List[str] = []


def find_group_badge(group: List[str]) -> str:
    elf_1: str = group[0]
    elf_2: str = group[1]
    elf_3: str = group[2]
    for char in elf_1:
        if char in elf_2 and char in elf_3:
            return char


while line:
    rucksack = line.strip()
    group.append(rucksack)
    if len(group) == 3:
        common.append(find_group_badge(group))
        group.clear()
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
