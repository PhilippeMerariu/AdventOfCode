
pastnbs = []
found = False
res = ''
file = open('input9.txt')
line = file.readline().replace('\n', '')
while line:
    found = False
    if len(pastnbs) < 25:
        pastnbs.append(int(line))
    else:
        for nb1 in pastnbs:
            for nb2 in pastnbs:
                if nb1 != nb2 and nb1 + nb2 == int(line):
                    found = True

        if not found:
            res = line
            break
        elif found:
            pastnbs = pastnbs[1:]
            pastnbs.append(int(line))
    line = file.readline().replace('\n', '')
file.close()

print('Result: ' + res)

