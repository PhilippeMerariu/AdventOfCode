import math

file = open('input6.txt')
line = file.readline()

result = 0

data = []

while line:
    line = line.strip('\n')
    data.append(line)
    line = file.readline()
file.close()

formatted_data = []
for d in data[:-1]:
    d = d.replace(' ', ' ')
    formatted_data.append(d)
formatted_data.append(data[-1])

values = []
for i in range(len(formatted_data[0]) - 1, -1, -1):
    val = ""
    for fd in formatted_data[:-1]:
        val += fd[i]
    if not val.replace(' ', ''):
        values.append(formatted_data[-1][i + 1])
    else:
        values.append(val)
values.append(formatted_data[-1][0])

terms = []
solutions = []
for v in values:
    if v == '+':
        solutions.append(sum(terms))
        terms.clear()
    elif v == '*':
        solutions.append(math.prod(terms))
        terms.clear()
    else:
        terms.append(int(v))

result = sum(solutions)

print(f"ANSWER = {result}")
