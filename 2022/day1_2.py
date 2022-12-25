from typing import List

file = open('input1.txt')
line = file.readline()

elves: List[int] = []
calories: int = 0


while line:
    if line == "\n":
        elves.append(calories)
        calories = 0
    else:
        calories += int(line.strip())
    line = file.readline()
file.close()

top3: int = 0

for i in range(3):
    top3 += max(elves)
    elves.remove(max(elves))

print("ANSWER = {0}".format(top3))
