from typing import List

file = open('input4.txt')
line = file.readline()

elf1: List[int] = []
elf2: List[int] = []
nb_encapsulated: int = 0


def generate_range(rng: str) -> List[int]:
    final_range: List[int] = []
    r: List[str] = rng.split('-')
    for i in range(int(r[0]), int(r[1]) + 1):
        final_range.append(i)
    return final_range


def is_encapsulated(e1: List[int], e2: List[int]) -> bool:
    if len(e1) < len(e2):
        if e2[0] <= e1[0] and e2[-1] >= e1[-1]:
            return True
    elif len(e2) < len(e1):
        if e1[0] <= e2[0] and e1[-1] >= e2[-1]:
            return True
    else:
        if e1[0] == e2[0] and e1[-1] == e2[-1]:
            return True
    return False


while line:
    pair = line.strip().split(',')
    elf1 = generate_range(pair[0])
    elf2 = generate_range(pair[1])
    if is_encapsulated(elf1, elf2):
        nb_encapsulated += 1
    line = file.readline()
file.close()

print("ANSWER = {0}".format(nb_encapsulated))
