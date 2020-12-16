def getRange(arr):
    ran = []
    for r in arr:
        min = int(r.split('-')[0])
        max = int(r.split('-')[1])
        for i in range(min, max+1):
            ran.append(i)
    return ran

def isFieldValid(value):
    for field in fields:
        if value in fields.get(field):
            return True
    return False

def findField(index, value):
    newFields = []
    for f in fieldOrder:
        newFields.append(f.copy())
    for field in fieldOrder[i]:
        if value not in fields.get(field):
            newFields[index].remove(field)
    return newFields.copy()

def removeField(field):
    for section in fieldOrder:
        if len(section) > 1 and section.__contains__(field):
            section.remove(field)

def isComplete():
    for section in fieldOrder:
        if len(section) > 1:
            return False
    return True

fields = {}
fieldOrder = []
myTicket = []
otherTickets = []
section = 0 # 0 --> fields, 1 --> my ticket, 2 --> other tickets

file = open('input16.txt')
line = file.readline()

while line:
    if line == '\n':
        section += 1
    else:
        line = line.replace('\n', '')
        if section == 0:
            line = line.split(':')
            fieldName = line[0]
            fieldRange = getRange(line[1].replace(' ','').split('or'))
            fields.update({fieldName: fieldRange})
        elif section == 1 and line != 'your ticket:':
            myTicket = line.split(',')
        elif section == 2 and line != 'nearby tickets:':
            tick = line.split(',')
            otherTickets.append(tick)
    line = file.readline()
file.close()

res = 1
validTickets = otherTickets.copy()

for ticket in otherTickets:
    for value in ticket:
        value = int(value)
        if not isFieldValid(value):
            validTickets.remove(ticket)

otherTickets = validTickets.copy()

f = []
for field in fields:
    f.append(field)
for i in range(0, len(fields)):
    fieldOrder.append(f.copy())

for i in range(0, len(fields)):
    for ticket in otherTickets:
        fieldOrder = findField(i, int(ticket[i]))
    if len(fieldOrder[i]) == 1:
        removeField(fieldOrder[i][0])



while not isComplete():
    for fieldlist in fieldOrder:
        if len(fieldlist) == 1:
            removeField(fieldlist[0])

for i in range(len(fields)):
    if fieldOrder[i][0].startswith('departure'):
        res *= int(myTicket[i])

print("Result: " + str(res) )
