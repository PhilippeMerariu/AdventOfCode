from typing import List

file = open('input1.txt')
line = file.readline()

numbers: List[int] = []

while line:
    numbers.append(int(line))
    line = file.readline()
file.close()

sums: List[int] = []

for i in range(len(numbers)):
    try:
        sums.append(numbers[i] + numbers[i+1] + numbers[i+2])
    except:
        pass

prev: int = None
increases: int = 0
for curr in sums:
    if prev is None:
        prev = curr
    else:
        if curr > prev:
            increases += 1
    prev = curr

print("ANSWER = {0}".format(increases))