import itertools

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

#for k, v in machine.items():
#    print(f"{k} --> buttons={v['buttons']} || joltages={v['joltages']}")

def compute_lights(btns: tuple[list[int]], lights: str) -> str:
    ll = list(lights)
    for b in btns:
        for l in b:
            if ll[l] == '.':
                ll[l] = '#'
            else:
                ll[l] = '.'
    return ''.join(ll)


for m in machine:
    pattern = m['pattern']
    buttons = m['buttons']
    nb_clicks = 1
    lights = '.' * len(pattern)
    while lights != pattern:
        combos = itertools.combinations(buttons, nb_clicks)
        for c in combos:
            lights = compute_lights(c, '.' * len(pattern))
            #print(f"pattern={key} || clicks={nb_clicks} || combo={c} || lights={lights}")
            if lights == pattern:
                #print(f'FOUND LIGHT PATTERN!!!! ==> {c} with {nb_clicks} clicks')
                result += nb_clicks
                break
        nb_clicks += 1


print(f"ANSWER = {result}")
