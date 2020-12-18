def calculate(eq):
    count = 0
    for symb in eq:

        if symb.isdigit():
            order.get(count)[0].append(int(symb))
        elif symb in ['+', '*']:
            order.get(count)[1].append(symb)
        elif symb == '(':
            nb.clear()
            op.clear()
            count += 1
            order.update({count: [nb.copy(), op.copy()]})
        elif symb == ')':
            nb.clear()
            op.clear()
            count -= 1
            order.get(count)[0].append(operation())
            order.pop(count+1)
    return operation()

def operation():
    data = order.get(max(order))
    nbs = data[0]
    ops = data[1]
    res = nbs[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += nbs[i+1]
        else:
            res *= nbs[i+1]
    return res


op = []
nb = []
order = {0: [nb.copy(), op.copy()]}
total = 0

file = open('input18.txt')
line = file.readline().replace('\n', '')
#line = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 '

#total += calculate(line.replace(' ', ''))
while line:
    total += calculate(line.replace(' ', ''))
    print("subtotal: " + str(total))
    nb.clear()
    op.clear()
    order = {0: [nb.copy(), op.copy()]}
    line = file.readline().replace('\n', '')
file.close()

print("Result: " + str(total))

