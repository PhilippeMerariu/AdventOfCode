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

fields = {}
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

res = 0

for ticket in otherTickets:
    for value in ticket:
        value = int(value)
        if not isFieldValid(value):
            res += value



print("Result: " + str(res) )
