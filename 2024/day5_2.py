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

def fix_update(update):
    fixed_update = [update[0]]
    useful_rules = []
    for r in rules:
        if r[0] in update or r[1] in update:
            useful_rules.append(r)
    for page in update[1:]:
        before = []
        after = []
        for ur in useful_rules:
            if ur[0] == page:
                after.append(ur[1])
            elif ur[1] == page:
                before.append(ur[0])
        if not after:  # nothing comes before this page (it is first)
            fixed_update.append(page)
        elif not before:  # nothing comes after this page (it is last)
            fixed_update.insert(0, page)
        else:
            before_idxs = []
            for b in before:
                try:
                    before_idxs.append(fixed_update.index(b))
                except ValueError:
                    pass
            if before_idxs:
                fixed_update.insert(max(before_idxs) + 1, page)
            else:
                fixed_update.insert(0, page)
    return fixed_update

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

for upt in updates:
    if not is_valid(upt):
        fixed_upt = fix_update(upt)
        mid = int(len(fixed_upt) / 2)
        result += fixed_upt[mid]

print(f"ANSWER = {result}")
