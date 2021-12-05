from typing import List

file = open('input4.txt')
line = file.readline().strip()

while line:
    line = file.readline().strip()
file.close()



print("ANSWER = {0}".format())