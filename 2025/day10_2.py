from fractions import Fraction
from itertools import product
from math import lcm

file = open('input10.txt')
line = file.readline()

result = 0

machine = []

while line:
    line = line.strip('\n')
    light_pattern = ''
    buttons = []
    joltages = []
    elements = line.split(' ')
    for elem in elements:
        if elem[0] == '[':
            light_pattern = elem[1:-1]
        elif elem[0] == '(':
            buttons.append([int(b) for b in elem[1:-1].split(',')])
        else:
            joltages = [int(j) for j in elem[1:-1].split(',')]
    machine.append({'pattern': light_pattern, 'buttons': buttons, 'joltages': joltages})
    line = file.readline()
file.close()

def solve_machine(target, buttons):
    n = len(target)
    m = len(buttons)

    max_presses = [min(target[c] for c in b) for b in buttons]
    order = sorted(range(m), key=lambda j: -max_presses[j])

    aug = [[Fraction(0)] * (m + 1) for _ in range(n)]
    for col, b_idx in enumerate(order):
        for c in buttons[b_idx]:
            aug[c][col] = Fraction(1)
    for c in range(n):
        aug[c][m] = Fraction(target[c])

    pivots = []
    row = 0
    for col in range(m):
        p = next((i for i in range(row, n) if aug[i][col] != 0), None)
        if p is None:
            continue
        aug[row], aug[p] = aug[p], aug[row]
        pivot_value = aug[row][col]
        aug[row] = [v / pivot_value for v in aug[row]]
        for i in range(n):
            if i != row and aug[i][col] != 0:
                f = aug[i][col]
                aug[i] = [a - f * b for a, b in zip(aug[i], aug[row])]
        pivots.append(col)
        row += 1

    for leftover in aug[len(pivots):]:
        if leftover[m] != 0:
            return None  # contradictory equations, no solution at all

    free = [j for j in range(m) if j not in pivots]

    equations = []
    for i, col in enumerate(pivots):
        den = lcm(aug[i][m].denominator, *[aug[i][j].denominator for j in free])
        equations.append((int(aug[i][m] * den),
                          [int(aug[i][j] * den) for j in free],
                          den))

    best = None
    for values in product(*[range(max_presses[order[j]] + 1) for j in free]):
        total = sum(values)
        for rhs, coefs, den in equations:
            v = rhs
            for coef, x in zip(coefs, values):
                v -= coef * x
            if v < 0 or v % den:
                break  # negative or fractional number of presses
            total += v // den
        else:
            if best is None or total < best:
                best = total
    return best


result = 0
unsolvable = []
for count, m in enumerate(machine, 1):
    print(f"Progress: {count}/{len(machine)}", end='\r', flush=True)
    clicks = solve_machine(m['joltages'], m['buttons'])
    if clicks is None:
        unsolvable.append(count)
    else:
        result += clicks

print()
if unsolvable:
    print(f"NO SOLUTION for machines: {unsolvable}")
print(f"ANSWER = {result}")
