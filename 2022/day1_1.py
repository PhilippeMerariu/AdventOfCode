file = open('input1.txt')
line = file.readline()

calories: int = 0
max_calories: int = 0

while line:
    if line == "\n":
        if calories > max_calories:
            max_calories = calories
        calories = 0
    else:
        calories += int(line.strip())
    line = file.readline()
file.close()

print("ANSWER = {0}".format(max_calories))
