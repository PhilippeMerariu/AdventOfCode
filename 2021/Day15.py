
file = open('input15_test.txt')
line = file.readline()

while line:
    line = file.readline()
file.close()

answer: int = 0
print("ANSWER = {0}".format(answer))
