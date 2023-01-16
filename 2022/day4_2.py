from typing import List

file = open('input4.txt')
line = file.readline()

elf1: List[int] = []
elf2: List[int] = []
nb_overlap: int = 0


def generate_range(rng: str) -> List[int]:
    final_range: List[int] = []
    r: List[str] = rng.split('-')
    for i in range(int(r[0]), int(r[1]) + 1):
        final_range.append(i)
    return final_range


def is_overlap(e1: List[int], e2: List[int]) -> bool:
    e1.reverse()
    for nb in e1:
        if nb in e2:
            return True
    return False


while line:
    pair = line.strip().split(',')
    elf1 = generate_range(pair[0])
    elf2 = generate_range(pair[1])
    if is_overlap(elf1, elf2):
        nb_overlap += 1
    line = file.readline()
file.close()

print("ANSWER = {0}".format(nb_overlap))
