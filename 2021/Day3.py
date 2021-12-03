from typing import List

file = open('input3.txt')
line = file.readline().strip()

gamma: int = -1
gamma_bits: str = ''
epsilon: int = -1
epsilon_bits: str = ''

occurrences: List[List[int]] = []

for bit in line:
    occurrences.append([0, 0])

while line:
    for i in range(len(line)):
        occurrences[i][int(line[i])] += 1
    line = file.readline().strip()
file.close()

for o in occurrences:
    if o[0] > o[1]:
        gamma_bits += '0'
        epsilon_bits += '1'
    else:
        gamma_bits += '1'
        epsilon_bits += '0'

gamma = int(gamma_bits, 2)
epsilon = int(epsilon_bits, 2)

power = gamma * epsilon

print("ANSWER = {0}".format(power))
