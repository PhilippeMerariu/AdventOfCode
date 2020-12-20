# def getAllPossibilities():
#     for index in modRules:
#         r = modRules.get(index)
#         if len(r) > 1:
import copy

rules = {}
messages = []
section = 0 # 0 --> rules, 1 --> messages

file = open('input19.txt')
line = file.readline()

while line:
    if line == '\n':
        section = 1
        line = file.readline()
    line = line.replace('\n', '')
    if section == 0:
        ruleNb, subrules = line.split(': ')
        subrules = [s.split(' ') for s in subrules.split(' | ')]
        rules[int(ruleNb)] = subrules
    else:
        messages.append(line)
    line = file.readline()
file.close()

def match_rule(i, line):
    for subrule in rules[i]:
        if not subrule[0].startswith('"'):
            yield from match_subrule(subrule, 0, line)
        elif line and subrule[0][1] == line[0]:
            yield line[1:]


def match_subrule(subrule, j, line):
    if j >= len(subrule):
        yield line
        return
    for match in match_rule(int(subrule[j]), line):
        yield from match_subrule(subrule, j + 1, match)


count = sum("" in match_rule(0, msg) for msg in messages)

print(count)

# while line:
#     if line == '\n':
#         section += 1
#         line = file.readline()
#     line = line.replace('\n', '')
#     if section == 0:
#         rule = line.split(':')
#         ruleNb = int(rule[0])
#         ruleStr = rule[1].strip().replace('"', '').split(' | ')
#         if ruleStr[0].isalpha():
#                 ruleStr = ruleStr[0]
#         rules.update({ruleNb: ruleStr})
#     else:
#         messages.append(line)
#     line = file.readline()
# file.close()
#
# changes = []
# changed = True
# modRules = []

# while changed:
#     changed = False
#     for index in rules:
#         r = rules.get(index)
#         for subr in r:
#             values = subr.split(' ')
#             for i in range(len(values)):
#                 val = values[i]
#                 try:
#                     modRules.insert(i, rules.get(int(val)))
#                 except:
#                     print("not a subrule")
#             rules[index] = modRules.copy()
#             modRules.clear()


# while changed:
#     changed = False
#
#     # change number to letter
#     for index in rules:
#         r = rules.get(index)
#         mr = modRules.get(index)
#         if len(r) > 1:
#             for i in range(len(r)):
#                 if r[i].isdigit():
#                     try:
#                         if rules.get(int(r[i])).isalpha():
#                             mr[i] = rules.get(int(r[i]))
#                             changed = True
#                             if i > 0 and mr[i].isalpha() and mr[i-1].isalpha():
#                                 changes.append([index, i-1])
#                     except:
#                         print("not a string...")
#
#     # merge characters
#     offset = 0
#     lastIndex = -1
#     for change in changes:
#         rindex = change[0]
#         if lastIndex != rindex:
#             offset = 0
#         strindex = change[1] - offset
#         rule = modRules.get(rindex)
#         combined = rule[strindex] + rule[strindex+1]
#         rule.pop(strindex)
#         rule.pop(strindex)
#         rule.insert(strindex, combined)
#         offset += 1
#         lastIndex = rindex
#
#     rules = copy.deepcopy(modRules)



#
# print("Result: " )

