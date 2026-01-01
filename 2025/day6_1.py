file = open('input6.txt')
line = file.readline()

result = 0

problems = []


while line:
    line = line.strip('\n')
    terms = line.split(' ')
    for _ in range(terms.count('')):
        terms.remove('')
    problems.append(terms)
    line = file.readline()
file.close()

operators = problems[-1]
problems = problems[:-1]
solutions = [0 if op == '+' else 1 for op in operators]

for prob in problems:
    for i in range(len(prob)):
        if operators[i] == '+':
            solutions[i] += int(prob[i])
        else:
            solutions[i] *= int(prob[i])

result = sum(solutions)

print(f"ANSWER = {result}")
