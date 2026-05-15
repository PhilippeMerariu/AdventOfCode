from collections import deque

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

#def compute_jolts(btns: tuple[list[int]], jolts: list[int], expected: list[int]) -> list[int]:
#    for b in btns:
#        for j in b:
#            jolts[j] += 1
#            if jolts[j] > expected[j]:
#                return []
#    return jolts

def solve_machine(pattern, buttons):
    num_counters = len(pattern)
    btn_effects = buttons

    best_presses = float('inf')

    def dfs(btn_idx, current_jolts, current_presses):
        nonlocal best_presses

        if current_presses >= best_presses:
            return

        if btn_idx == len(buttons):
            if current_jolts == pattern:
                best_presses = min(best_presses, current_presses)
            return

        btn_maxes = []
        for i in range(btn_idx, len(buttons)):
            m = min(pattern[rc] - current_jolts[rc] for rc in btn_effects[i])
            btn_maxes.append(max(0, m))

        for c in range(num_counters):
            needed = pattern[c] - current_jolts[c]
            if needed < 0:
                return

            max_supply = 0
            for idx, i in enumerate(range(btn_idx, len(buttons))):
                if c in btn_effects[i]:
                    max_supply += btn_maxes[idx]

            if max_supply < needed:
                return

        curr_max = btn_maxes[0]
        for p in range(curr_max + 1):
            next_jolts = list(current_jolts)
            for c in btn_effects[btn_idx]:
                next_jolts[c] += p

            dfs(btn_idx + 1, next_jolts, current_presses + p)

    dfs(0, [0] * num_counters, 0)
    return best_presses


count = 1
for m in machine:
    print(f"Progress: {count+1}/{len(machine)}", end='\r', flush=True) 
    pattern = m['joltages']
    buttons = m['buttons']
    #result += solve_machine(pattern, buttons)
    clicks = solve_machine(pattern, buttons)
    if clicks != float('inf'):
        result += clicks
    count += 1

    #nb_clicks = 1
    #jolts = [0] * len(pattern)
    #while jolts != pattern:
    #    print(f"Progress: {count+1}/{len(machine)} || Clicks={nb_clicks}", end='\r', flush=True)
    #    combos = itertools.combinations_with_replacement(buttons, nb_clicks)
    #    for c in combos:
    #        jolts = compute_jolts(c, [0] * len(pattern), pattern)
    #        #print(f"pattern={pattern} || clicks={nb_clicks} || combo={c} || lights={jolts}")
    #        if jolts == pattern:
    #            #print(f'FOUND LIGHT PATTERN!!!! ==> {c} with {nb_clicks} clicks')
    #            result += nb_clicks
    #            count += 1
    #            break
    #    nb_clicks += 1

print()
print(f"ANSWER = {result}")
