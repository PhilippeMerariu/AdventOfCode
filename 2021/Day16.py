
file = open('input16_test.txt')
line = file.readline().strip()

binary: bin = bin(int(line, 16))
print(binary)



answer: int = 0
print("ANSWER = {0}".format(answer))
