from typing import List, Tuple

file = open('input2.txt')
line = file.readline()

# elf values
A: int = 1
B: int = 2
C: int = 3

# result
X: int = 0
Y: int = 3
Z: int = 6

winning_hand: List[Tuple[str, str]] = [("A", "Y"), ("B", "Z"), ("C", "X")]
score: int = 0


def evaluate_round(elf: str, result: str) -> int:
    if result == 'Y':  # tie
        return eval(elf) + eval(result)
    if result == 'X':  # loose
        if elf == 'A':
            return C + eval(result)
        if elf == 'B':
            return A + eval(result)
        if elf == 'C':
            return B + eval(result)
    if result == 'Z':  # win
        if elf == 'A':
            return B + eval(result)
        if elf == 'B':
            return C + eval(result)
        if elf == 'C':
            return A + eval(result)


while line:
    hand: List[str] = line.strip().split(" ")
    score += evaluate_round(hand[0], hand[1])
    line = file.readline()
file.close()

print("ANSWER = {0}".format(score))
