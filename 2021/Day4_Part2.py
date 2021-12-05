from typing import List

file = open('input1.txt')
line = file.readline()

numbers: List[int] = []

while line:
    numbers.append(int(line))
    line = file.readline()
file.close()

prev: int = None
increases: int = 0
for curr in numbers:
    if prev is None:
        prev = curr
    else:
        if curr > prev:
            increases += 1
    prev = curr

print("ANSWER = {0}".format(increases))