from typing import List, Dict

file = open('input13_test.txt')
line = file.readline().strip()

while line:
    line = file.readline().strip()
file.close()

answer: int = 0
print("ANSWER = {0}".format(answer))
