file = open('input5.txt')
line = file.readline()

rules = []
updates = []
result = 0

def is_valid(update):
    for r in rules:
        try:
            idx1 = update.index(r[0])
            idx2 = update.index(r[1])
            if idx2 < idx1:
                return False
        except ValueError:
            pass
    return True

while line:
    line = line.strip('\n')
    if '|' in line:
        rule = line.split('|')
        rule = [int(x) for x in rule]
        rules.append(tuple(rule))
    elif ',' in line:
        update = line.split(',')
        update = [int(x) for x in update]
        updates.append(update)

    line = file.readline()
file.close()

print("rules:", rules)
print("updates:", updates)

for upt in updates:
    if is_valid(upt):
        mid = int(len(upt) / 2)
        result += upt[mid]

print(f"ANSWER = {result}")
