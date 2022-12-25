from typing import List, Tuple

file = open('input2.txt')
line = file.readline()

# elf values
A: int = 1
B: int = 2
C: int = 3

# my values
X: int = 1
Y: int = 2
Z: int = 3

# result
LOSS: int = 0
TIE: int = 3
WIN: int = 6

winning_hand: List[Tuple[str, str]] = [("A", "Y"), ("B", "Z"), ("C", "X")]
score: int = 0


def evaluate_round(elf: str, me: str) -> int:
    if eval(elf) == eval(me):
        return eval(me) + TIE
    if (elf, me) in winning_hand:
        return eval(me) + WIN
    return eval(me) + LOSS


while line:
    hand: List[str] = line.strip().split(" ")
    score += evaluate_round(hand[0], hand[1])
    line = file.readline()
file.close()

print("ANSWER = {0}".format(score))
