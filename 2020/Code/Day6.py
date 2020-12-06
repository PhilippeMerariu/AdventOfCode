file = open('input6.txt')
line = file.readline()

answers = []
total = 0

while line:
    if line == '\n':
        total += len(answers)
        answers = []
    else:
        line = line.replace('\n', '')
        for char in line:
            if char not in answers:
                answers.append(char)
    line = file.readline()
file.close()

total += len(answers)

print('Result: ' + str(total))

