file = open('input7.txt')
line = file.readline()

values = []
terms = []

def evaluate_eq(eq) -> int:
    nb1 = eq[0]
    op = eq[1]
    nb2 = eq[2]
    eq = eq[3:]
    total = eval(f"{nb1}{op}{nb2}")
    while len(eq):
        next_op = eq[0]
        next_nb = eq[1]
        eq = eq[2:]
        total = eval(f"{total}{next_op}{next_nb}")
    return total

while line:
    line = line.strip('\n')
    val, numbers = line.split(':')
    values.append(val)
    terms.append(numbers.split(' ')[1:])
    line = file.readline()
file.close()

result = 0

for i in range(len(values)):
    nb_terms = len(terms[i])
    nb_operators = nb_terms - 1
    nb_combinations = 2 ** nb_operators
    for j in range(nb_combinations):
        bin_terms = format(j, f'0{nb_operators}b')
        operators = []
        for b in bin_terms:
            operators.append('+' if b == '0' else '*')
        eq = []
        for k in range(len(operators)):
            eq.append(terms[i][k])
            eq.append(operators[k])
        eq.append(terms[i][-1])
        if evaluate_eq(eq) == int(values[i]):
            result += int(values[i])
            print(f"FOUND! {values[i]} = {eq}")
            break


print(f"ANSWER = {result}")
