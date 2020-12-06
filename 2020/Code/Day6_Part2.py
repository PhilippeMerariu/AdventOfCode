file = open('input6.txt')
line = file.readline()

answers = []
incorrect = []
total = 0
first = True
count = 0

while line:
    if line == '\n':
        total += len(answers)
        answers = []
        incorrect = []
        first = True
    else:
        line = line.replace('\n', '')
        if first:
            for char in line:
                answers.append(char)
            first = False
        else:
            incorrect = []
            for letter in answers:
                # print(letter)
                if letter not in line:
                    incorrect.append(letter)
                    # answers.remove(letter)
            for bad in incorrect:
                answers.remove(bad)
    line = file.readline()
    count += 1
file.close()

total += len(answers)

print('Result: ' + str(total))

