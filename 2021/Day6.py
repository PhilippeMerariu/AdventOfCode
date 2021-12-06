from typing import List

file = open('input6.txt')
line = file.readline().strip()


while line:
    line = file.readline()
file.close()

answer: int = 0


print("ANSWER = {0}".format(answer))
